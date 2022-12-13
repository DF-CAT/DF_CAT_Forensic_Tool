import json
import os
import csv
import threading
import tkinter as tk
import tkinter.ttk
from time import sleep
from tkinter import *


def Browser_Downloads(userprofile,json_path, CSV, csv_path):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile,json_path, CSV, csv_path,))
    testThread.start()
    testThread.join()


def Callback_Start(userprofile,json_path, CSV, csv_path):
    js_data = []
    with open(r"{}\Browser_Downloads.json".format(userprofile), encoding="utf-16") as infile:
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
    label = Label(pbarroot, text="Browser Downloads 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum=maximum, length=150, mode='determinate')
    pbar.pack()

    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, js_data,json_path, CSV, csv_path,))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()


def Function_Start(pbarroot, pbar, js_data,json_path, CSV, csv_path):import json
import os
import csv
import threading
import tkinter as tk
import tkinter.ttk
from time import sleep
from tkinter import *


def Browser_Downloads(userprofile,json_path, CSV, csv_path):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile,json_path, CSV, csv_path,))
    testThread.start()
    testThread.join()


def Callback_Start(userprofile,json_path, CSV, csv_path):
    js_data = []
    with open(r"{}\Browser_Downloads.json".format(userprofile), encoding="utf-16") as infile:
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
    label = Label(pbarroot, text="Browser Downloads 수집 중\n", font=('맑은 고딕', 11))
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
    data = {"ART0002": {"version": "1.0.4", "name": "Browser_Downloads", "isEvent": False, "data": []}}

    try:
        for item in js_data:
            sleep(0.001)
            pbar.step()
            itemd = item.copy()

            Ndel = ["Filename", "Download URL 1", "Start Time", "End Time", "Download Size", "Full Path Filename",
                    "Web Browser"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['name'] = item.pop('Filename')
            item['url'] = item.pop('Download URL 1')
            item['browser'] = item.pop('Web Browser')
            item['start_time'] = item.pop('Start Time')
            item['end_time'] = item.pop('End Time')
            item['size'] = item.pop('Download Size')
            item['path'] = item.pop('Full Path Filename')
            item['timeline_items'] = []

            for key in item:
                if item[key] is not None:
                    data["ART0002"]["data"].append(item)
                    break

            if item["start_time"] is None and item["end_time"] is None:
                continue

            if item["start_time"] is None:
                item["timeline_items"].append({
                    "name": "end_time",
                    "start_time": item["end_time"],
                    "end_time": item["end_time"]})
            elif item["end_time"] is None:
                item["timeline_items"].append({
                    "name": "start_time",
                    "start_time": item["start_time"],
                    "end_time": item["start_time"]})

            else:
                item["timeline_items"].append({
                    "name": "",
                    "start_time": item["start_time"],
                    "end_time": item["end_time"]})

        if json_path is not None:
            with open(r"{}/ART0002_Browser_Downloads.json".format(json_path), 'w', encoding="utf-8") as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)

        if CSV != 0:
            with open(r"{}/ART0002_Browser_Downloads.csv".format(csv_path), 'w', newline = '', encoding='ANSI') as output_file:
                f = csv.writer(output_file)

                # csv 파일에 header 추가
                f.writerow(["name", "url", "browser", "start_time", "end_time", "size", "path"])

                # write each row of a json file
                for datum in data["ART0002"]["data"]:
                    sleep(0.001)
                    pbar.step()
                    f.writerow([datum["name"], datum["url"], datum["browser"], datum["start_time"], datum["end_time"], datum["size"], datum["path"]])
        
    except:
        pass

    pbarroot.destroy()
