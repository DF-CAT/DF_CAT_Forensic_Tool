import json
import os
import csv
import threading
import tkinter as tk
import tkinter.ttk
from time import sleep
from tkinter import *


def Bookmarks(userprofile,json_path, CSV, csv_path):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile,json_path, CSV, csv_path,))
    testThread.start()
    testThread.join()


def Callback_Start(userprofile,json_path, CSV, csv_path):
    js_data = []
    with open(r"{}\Bookmarks.json".format(userprofile), encoding="utf-16") as infile:
        js_data = json.load(infile)
    maximum = len(js_data)

    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0, 0)

    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="Bookmarks 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum=maximum, length=150, mode='determinate')
    pbar.pack()

    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, js_data,json_path, CSV, csv_path,))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()


def Function_Start(pbarroot, pbar, js_data,json_path, CSV, csv_path):
    data = {"ART0060": {"name": "Bookmarks", "isEvent": False, "data": []}}

    try:
        for item in js_data:
            sleep(0.001)
            pbar.step()
            itemd = item.copy()

            Ndel = ["Title", "URL", "Folder Path", "Created Time", "Web Browser"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['name'] = item.pop('Title')
            item['url'] = item.pop('URL')
            item['path'] = item.pop('Folder Path')
            item['created_time'] = item.pop('Created Time')
            item['browser'] = item.pop('Web Browser')
            item['timeline_items'] = []

            for key in item:
                if item[key] is not None:
                    data["ART0060"]["data"].append(item)
                    break

            if item['created_time'] is not None:
                item["timeline_items"].append(
                    {"name": "created_time", "start_time": item['created_time'], "end_time": item['created_time']})

        if json_path is not None:
            with open(r"{}/ART0060_Bookmarks.json".format(json_path), 'w', encoding="utf-8") as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)
        
        if CSV != 0:
            with open(r"{}/ART0060_Bookmarks.csv".format(csv_path), 'w', newline = '', encoding='ANSI') as output_file:
                f = csv.writer(output_file)

                # csv 파일에 header 추가
                f.writerow(["name", "url", "path", "created_time", "browser"])

                # write each row of a json file
                for datum in data["ART0060"]["data"]:
                    sleep(0.001)
                    pbar.step()
                    f.writerow([datum["name"], datum["url"], datum["path"], datum["created_time"], datum["browser"]])

    except:
        pass

    pbarroot.destroy()
