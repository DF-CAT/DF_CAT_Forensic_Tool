import xmltodict
import json
import re
import csv

from tkinter import *
import tkinter.ttk
import tkinter as tk
import threading
from time import sleep
import os

def History_and_Download_History(userprofile,json_path, CSV, csv_path):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile, json_path, CSV, csv_path,))
    testThread.start()
    testThread.join()

def Callback_Start(userprofile,json_path, CSV, csv_path):
    csv_data = []
    with open("{}\\History_and_Download_History.xml".format(userprofile), encoding="utf-16") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        
    maximum = len(data_dict["browsing_history_items"]["item"])
    
    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0,0)
    
    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="Web History 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum = maximum, length=150, mode='determinate')
    pbar.pack()
    
    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, data_dict, json_path, CSV, csv_path,))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()

def Function_Start(pbarroot, pbar, data_dict,json_path, CSV, csv_path):
    data = {"ART0030": {"name": "Web_History", "isEvent": False, "data": []}}
    try:
        for item in data_dict["browsing_history_items"]["item"]:
            pbar.step()
            if item["url"] is None:
                continue

            if re.search("http?s|file", str(item["url"]), re.I) is None:
                continue

            itemd = item.copy()

            Ndel = ["url", "title", "visit_time", "web_browser"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['url'] = item.pop('url')
            item['title'] = item.pop('title')
            item['visited_time'] = item.pop('visit_time')
            item['browser'] = item.pop('web_browser')
            item['timeline_items'] = []

            for key in item:
                if item[key] is not None:
                    data["ART0030"]["data"].append(item)
                    break

            if item["visited_time"] is not None:
                item["timeline_items"].append(
                    {"name": "visited_time", "start_time": item["visited_time"], "end_time": item["visited_time"]})

        json_data = data

        if json_path is not None:
            with open(r"{}/ART0030_Web_History.json".format(json_path), "w", encoding='utf-8') as json_file:
                json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()
        
        if CSV != 0:
            with open(r"{}/ART0030_Web_History.csv".format(csv_path), 'w', newline = '', encoding='ANSI') as output_file:
                f = csv.writer(output_file)

                # csv 파일에 header 추가
                f.writerow(["url", "title", "visited_time", "browser"])

                # write each row of a json file
                for datum in data["ART0030"]["data"]:
                    pbar.step()
                    f.writerow([datum["url"], datum["title"], datum["visited_time"], datum["browser"]])

    except FileNotFoundError:
        pass
    except UnicodeError:
        pass
    
    pbarroot.destroy()
