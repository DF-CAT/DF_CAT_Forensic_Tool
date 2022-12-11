import json
import os
import threading
import tkinter as tk
import tkinter.ttk
from tkinter import *

import xmltodict


def Shell_Bags(userprofile):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile,))
    testThread.start()
    testThread.join()


def Callback_Start(userprofile):
    with open("{}\\Shell_Bags.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    maximum = len(data_dict["folders_list"]["item"])

    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "../../../../Downloads/artifact_parser/favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0, 0)

    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="Shell Bags 수집 중\n", font=('맑은 고딕', 11))
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
    data = {"ART0006": {"name": "Shell_Bags", "isEvent": False, "data": [], "timeline_items": []}}

    try:
        for item in data_dict["folders_list"]["item"]:
            pbar.step()
            itemd = item.copy()

            Ndel = ["path", "last_modified_time"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['path'] = item.pop('path')
            item['modified_time'] = item.pop('last_modified_time')

            for key in item:
                if item[key] is not None:
                    data["ART0006"]["data"].append(item)
                    break

            if item["modified_time"] is not None:
                data["ART0006"]["timeline_items"].append({"name": "path", "start_time": item["modified_time"],
                                                          "end_time": item["modified_time"]})

        json_data = data

        with open("ART0006_Shell_Bags.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()
            pbarroot.destroy()

    except:
        pass
