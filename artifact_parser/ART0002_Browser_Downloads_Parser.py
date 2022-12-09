import json

from tkinter import *
import tkinter.ttk
import tkinter as tk
import threading
from time import sleep
import os

def Browser_Downloads(userprofile):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile, ))
    testThread.start()
    testThread.join()

def Callback_Start(userprofile):
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
    pbarroot.resizable(0,0)
    
    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="Browser Downloads 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum = maximum, length=150, mode='determinate')
    pbar.pack()
    
    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)
    
    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, js_data, ))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()

def Function_Start(pbarroot, pbar, js_data):
    data = {"ART0002": {"name": "Browser_Downloads", "isEvent": False, "data": []}}

    try:
        for item in js_data:
            sleep(0.001)
            pbar.step()
            itemd = item.copy()

            Ndel = ["Filename", "Download URL 1", "Start Time", "End Time", "Download Size", "Full Path Filename", "Web Browser"]

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

            for key in item:
                if item[key] is not None:
                    data["ART0002"]["data"].append(item)
                    break

        with open("ART0002_Browser_Downloads.json", 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)

    except:
        pass
    
    pbarroot.destroy()