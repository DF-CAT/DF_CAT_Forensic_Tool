import json
import os
import threading
import csv
import tkinter as tk
import tkinter.ttk
from tkinter import *

import xmltodict


def Jump_Lists(userprofile,json_path, CSV, csv_path):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile,json_path, CSV, csv_path,))
    testThread.start()
    testThread.join()


def Callback_Start(userprofile,json_path, CSV, csv_path):
    with open("{}\\Jump_Lists.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    maximum = len(data_dict["jump_lists"]["item"])

    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0, 0)

    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="Jump Lists 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum=maximum, length=150, mode='determinate')
    pbar.pack()

    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, data_dict,json_path, CSV, csv_path,))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()


def Function_Start(pbarroot, pbar, data_dict,json_path, CSV, csv_path):
    data = {"ART0008": {"name": "Jump_Lists", "isEvent": False, "data": []}}

    try:
        for item in data_dict["jump_lists"]["item"]:
            pbar.step()
            itemd = item.copy()

            Ndel = ["filename", "full_path", "accessed_time"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['name'] = item.pop('filename')
            item['path'] = item.pop('full_path')
            item['accessed_time'] = item.pop('accessed_time')
            item['timeline_items'] = []

            for key in item:
                if item[key] is not None:
                    data["ART0008"]["data"].append(item)
                    break

            if item["accessed_time"] is not None:
                item["timeline_items"].append(
                    {"name": "accessed_time", "start_time": item["accessed_time"], "end_time": item["accessed_time"]})

        json_data = data

        if json_path is not None:
            with open(r"{}/ART0008_Jump_Lists.json".format(json_path), "w", encoding='utf-8') as json_file:
                json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()
        
        if CSV != 0:
            with open(r"{}/ART0008_Jump_Lists.csv".format(csv_path), 'w', newline = '', encoding='ANSI') as output_file:
                f = csv.writer(output_file)

                # csv 파일에 header 추가
                f.writerow(["name", "path", "accessed_time"])

                # write each row of a json file
                for datum in data["ART0008"]["data"]:
                    pbar.step()
                    f.writerow([datum["name"], datum["path"], datum["accessed_time"]])

    except:
        pass
    
    pbarroot.destroy()
