import csv
import json
import os
import re

from tkinter import *
import tkinter.ttk
import tkinter as tk
import threading
from time import sleep
import os

def Prefetch(csv_files):
    testThread = threading.Thread(target=Callback_Start, args=(csv_files, ))
    testThread.start()
    testThread.join()

def Callback_Start(csv_files):
    csv_data = []
    for csv_file in csv_files:
        try:
            with open(csv_file, 'rt', encoding="utf-8") as f:
                csvReader = csv.DictReader(f)

                for rows in csvReader:
                    csv_data.append(rows)
        except:
            pass
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
    label = Label(pbarroot, text="Prefetch 수집 중\n", font=('맑은 고딕', 11))
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
    data = {"ART0009": {"name": "Prefetch", "isEvent": False, "data": []}}
    exts = '''[.]exe|[.]pdf|[.]hwp|[.]doc|[.]docm|[.]docx|[.]dot|[.]dotx|[.]csv|[.]ppt|[.]pptm|[.]pptx|[.]xlm|[
    .]xls|[.]xlsm|[.]xlsx|[.]zip|[.]rar|[.]7z|[.]txt '''

    for item in csv_data:
        sleep(0.001)
        pbar.step()
        itemd = item.copy()

        Ndel = ["ExecutableName", "FilesLoaded", "LastRun"]

        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]

        my_list = item["FilesLoaded"].split(',')
        files = []

        for file in my_list:
            if re.search(exts, str(os.path.basename(file)), re.I) is not None:
                files.append(os.path.basename(file))

        if not files:
            continue
        item["FilesLoaded"] = files
        item['name'] = item.pop('ExecutableName')
        item['executed_time'] = item.pop('LastRun')
        item["loaded_files"] = item.pop("FilesLoaded")

        for key in item:
            if item[key] is not None:
                data["ART0009"]["data"].append(item)
                break

    with open(r"ART0009_Prefetch.json", "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        json_file.close()
        pbarroot.destroy()
