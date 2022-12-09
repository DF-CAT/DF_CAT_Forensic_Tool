import csv
import json

from tkinter import *
import tkinter.ttk
import tkinter as tk
import threading
from time import sleep
import os

def Recycle_Bin(userprofile):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile, ))
    testThread.start()
    testThread.join()

def Callback_Start(userprofile):
    csv_data = []
    with open("{}\\Recycle_Bin.csv".format(userprofile), 'rt', encoding="utf-8") as f:
        csvReader = csv.DictReader(f)
        
        for rows in csvReader:
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
    label = Label(pbarroot, text="Recycle Bin 수집 중\n", font=('맑은 고딕', 11))
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
    data = {"ART0033": {"name": "Recycle_Bin", "isEvent": False, "data": []}}
    try:
        for item in csv_data:
            sleep(0.01)
            pbar.step()
            itemd = item.copy()

            Ndel = ["FileName", "DeletedOn"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['name'] = item.pop('FileName')
            item['deleted_time'] = item.pop('DeletedOn')

            for key in item:
                if item[key] is not None:
                    data["ART0033"]["data"].append(item)
                    break

        with open(r"ART0033_Recycle_Bin.json", "w", encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
            json_file.close()
            pbarroot.destroy()

    except FileNotFoundError:
        pass
