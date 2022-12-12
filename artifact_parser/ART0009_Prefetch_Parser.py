import json
import csv
import os
import re
import threading
import tkinter as tk
import tkinter.ttk
from tkinter import *

import xmltodict


def Prefetch(WinPrefetchView, userprofile, Ndata_list,json_path, CSV, csv_path):
    testThread = threading.Thread(target=Callback_Start, args=(WinPrefetchView, userprofile, Ndata_list,json_path, CSV, csv_path,))
    testThread.start()
    testThread.join()


def Callback_Start(WinPrefetchView, userprofile, Ndata_list,json_path, CSV, csv_path):
    maximum = len(Ndata_list)

    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
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

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, WinPrefetchView, userprofile, Ndata_list,json_path, CSV, csv_path,))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()


def Function_Start(pbarroot, pbar, WinPrefetchView, userprofile, Ndata_list,json_path, CSV, csv_path):
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

    data = {"ART0009": {"name": "Prefetch", "isEvent": False, "data": []}}
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
        item['timeline_items'] = []

        for key in item:
            if item[key] is not None:
                data["ART0009"]["data"].append(item)
                break

        if item["created_time"] is not None:
            item["timeline_items"].append(
                {"name": "created_time", "start_time": item["created_time"], "end_time": item["created_time"]})

        if item["modified_time"] is not None:
            item["timeline_items"].append(
                {"name": "modified_time", "start_time": item["modified_time"], "end_time": item["modified_time"]})

    if json_path is not None:
        with open(r"{}/ART0009_Prefetch.json".format(json_path), "w", encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
            json_file.close()

    if CSV != 0:
        with open(r"{}/ART0009_Prefetch.csv".format(csv_path), 'w', newline = '', encoding='ANSI') as output_file:
            
            f = csv.writer(output_file)
            # csv 파일에 header 추가
            f.writerow(["name", "created_time", "modified_time", "process_path", "records"])
            
            # write each row of a json file
            for datum in data["ART0009"]["data"]:
                pbar.step()
                f.writerow([datum["name"], datum["created_time"], datum["modified_time"], datum["process_path"], datum["records"]])

    pbarroot.destroy()
