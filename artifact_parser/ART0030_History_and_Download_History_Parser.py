import csv
import json
import re

from tkinter import *
import tkinter.ttk
import tkinter as tk
import threading
from time import sleep
import os

def History_and_Download_History(userprofile):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile, ))
    testThread.start()
    testThread.join()

def Callback_Start(userprofile):
    csv_data = []
    with open("{}\\History_and_Download_History.csv".format(userprofile), 'rt', encoding="euc-kr") as f:
        data_dict = csv.DictReader(f)
        
        for rows in data_dict:
            csv_data.append(rows)
    maximum = len(csv_data)
    
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

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, csv_data, ))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()

def Function_Start(pbarroot, pbar, csv_data):
    data = {"ART0030": {"name": "Web_History", "isEvent": False, "data": []}}
    try:
        for item in csv_data:
            sleep(0.01)
            pbar.step()
            if item["URL"] is None:
                continue

            if re.search("http?s|file", str(item["URL"]), re.I) is None:
                continue

            itemd = item.copy()

            Ndel = ["URL", "Title", "Visit Time", "Web Browser"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['url'] = item.pop('URL')
            item['title'] = item.pop('Title')
            item['visited_time'] = item.pop('Visit Time')
            item['browser'] = item.pop('Web Browser')

            for key in item:
                if item[key] is not None:
                    data["ART0030"]["data"].append(item)
                    break

        json_data = data

        with open("ART0030_Web_History.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()
            pbarroot.destroy()

    except FileNotFoundError:
        pass
    except UnicodeError:
        pass
