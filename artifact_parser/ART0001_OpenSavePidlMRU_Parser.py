import json
import os
import threading
import tkinter as tk
import tkinter.ttk
from time import sleep
from tkinter import *

import xmltodict


def OpenSavePidlMRU(userprofile):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile,))
    testThread.start()
    testThread.join()


def Callback_Start(userprofile):
    with open(r"{}\OpenSavePidlMRU.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    maximum = len(data_dict["open_save_files_list"]["item"])

    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0, 0)

    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="OpenSavePidlMRU 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum=maximum, length=150, mode='determinate')
    pbar.pack()

    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, data_dict,))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()


def Function_Start(pbarroot, pbar, data_dict):
    data = {"ART0001": {"name": "OpenSavePidlMRU", "isEvent": False, "data": [], "timeline_items": []}}

    try:
        for item in data_dict["open_save_files_list"]["item"]:
            sleep(0.001)
            pbar.step()
            if item["filename"] is None:
                continue
            itemd = item.copy()

            Ndel = ["filename", "extension", "open_time", "file_modified_time", "file_created_time", "file_size"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['name'] = item.pop('filename')
            item['extension'] = item.pop('extension')
            item['open_time'] = item.pop('open_time')
            item['created_time'] = item.pop('file_created_time')
            item['modified_time'] = item.pop('file_modified_time')
            item['size'] = item.pop('file_size')

            for key in item:
                if item[key] is not None:
                    data["ART0001"]["data"].append(item)
                    break

            if item["open_time"] is not None:
                data["ART0001"]["timeline_items"].append(
                    {"name": "name", "start_time": item["open_time"], "end_time": item["modified_time"]})

        json_data = data

        with open("ART0001_OpenSavePidlMRU.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)
            json_file.close()

    except:
        pass

    pbarroot.destroy()
