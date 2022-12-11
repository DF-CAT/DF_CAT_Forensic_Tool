import json
import os
import re
import threading
import tkinter as tk
import tkinter.ttk
from tkinter import *

import xmltodict


def Prefetch(WinPrefetchView, userprofile, Ndata_list):
    testThread = threading.Thread(target=Callback_Start, args=(WinPrefetchView, userprofile, Ndata_list,))
    testThread.start()
    testThread.join()


def Callback_Start(WinPrefetchView, userprofile, Ndata_list):
    maximum = len(Ndata_list)

    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "../../../../Downloads/artifact_parser/favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0, 0)

    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="Prefetch 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum=maximum, length=150, mode='determinate')
    pbar.pack()

    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, WinPrefetchView, userprofile, Ndata_list,))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()


def Function_Start(pbarroot, pbar, WinPrefetchView, userprofile, Ndata_list):
    for pf in Ndata_list:
        pbar.step()
        pf["records"] = []
        path = r"%systemdrive%\Windows\prefetch\{}".format(pf['filename'])
        os.popen(
            r'{0} /sxml {1} /prefetchfile "{2}"'.format(WinPrefetchView, userprofile + r"\prefetch.xml", path)).read()

        with open(userprofile + r"\prefetch.xml", encoding='utf-16') as x_file:
            data_list = xmltodict.parse(x_file.read())

            for i in data_list["prefetch_records"]["item"]:
                pf["records"].append({"name": i["filename"], "file_path": i["full_path"]})

    data = {"ART0009": {"name": "Prefetch", "isEvent": False, "data": [], "timeline_items": []}}
    exts = '''[.]exe|[.]pdf|[.]hwp|[.]doc|[.]docm|[.]docx|[.]dot|[.]dotx|[.]csv|[.]ppt|[.]pptm|[.]pptx|[.]xlm|[
    .]xls|[.]xlsm|[.]xlsx|[.]zip|[.]rar|[.]7z|[.]txt'''

    for item in Ndata_list:
        itemd = item.copy()

        Ndel = ["filename", "created_time", "modified_time", "process_path", "records"]

        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]

        files = []

        for file in item["records"]:
            if re.search(exts, file["name"], re.I) is not None:
                files.append(file)

        if not files:
            continue

        item["records"] = files
        item['name'] = item.pop('filename')
        item['created_time'] = item.pop('created_time')
        item['modified_time'] = item.pop('modified_time')
        item['process_path'] = item.pop('process_path')
        item['records'] = item.pop('records')

        for key in item:
            if item[key] is not None:
                data["ART0009"]["data"].append(item)
                break

        if item["modified_time"] is not None:
            data["ART0009"]["timeline_items"].append(
                {"name": "name", "start_time": item["modified_time"], "end_time": item["modified_time"]})

    with open(r"ART0009_Prefetch.json", "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        json_file.close()

    pbarroot.destroy()
