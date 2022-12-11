import csv
import json
import os
import threading
import tkinter as tk
import tkinter.ttk
from tkinter import *


def Shimcache(userprofile):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile,))
    testThread.start()
    testThread.join()


def Callback_Start(userprofile):
    csv_data = []
    with open("{}\\Shimcache.csv".format(userprofile), 'rt', encoding="utf-8") as f:
        csvReader = csv.DictReader(f)

        for rows in csvReader:
            csv_data.append(rows)
    maximum = len(csv_data)

    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "../../../../Downloads/artifact_parser/favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0, 0)

    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="ShimCache 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum=maximum, length=150, mode='determinate')
    pbar.pack()

    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, csv_data,))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()


def Function_Start(pbarroot, pbar, csv_data):
    data = {"ART0010": {"name": "ShimCache", "isEvent": False, "data": [], "timeline_items": []}}

    try:
        for item in csv_data:
            pbar.step()
            itemd = item.copy()

            Ndel = ["Path", "LastModifiedTimeUTC"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['path'] = item.pop('Path')
            item['modified_time'] = item.pop('LastModifiedTimeUTC')

            for key in item:
                if item[key] is not None:
                    data["ART0010"]["data"].append(item)
                    break

            if item["modified_time"] is not None:
                data["ART0010"]["timeline_items"].append(
                    {"name": "path", "start_time": item["modified_time"], "end_time": item["modified_time"]})

        with open(r"ART0010_ShimCache.json", "w", encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
            json_file.close()
            pbarroot.destroy()

    except:
        pass
