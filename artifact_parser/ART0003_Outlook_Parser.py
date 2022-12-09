import json

import xmltodict

from tkinter import *
import tkinter.ttk
import tkinter as tk
import threading
from time import sleep
import os

def Outlook(userprofile):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile, ))
    testThread.start()
    testThread.join()

def Callback_Start(userprofile):
    with open("{}\\Outlook.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    maximum = len(data_dict["outlook_attachments"]["item"])
    
    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0,0)
    
    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="E-mail Attachments 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum = maximum, length=150, mode='determinate')
    pbar.pack()
    
    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, data_dict, ))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()

def Function_Start(pbarroot, pbar, data_dict):
    data = {"ART0003": {"name": "E-mail_Attachments", "isEvent": False, "data": []}}

    try:
        for item in data_dict["outlook_attachments"]["item"]:
            sleep(0.01)
            pbar.step()
            itemd = item.copy()
            Ndel = ["filename", "from_email", "to_email", "message_delivery_time", "file_size", "domain"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            for key in item:
                if item[key] is not None:
                    item['name'] = item.pop('filename')
                    item['from_email'] = item.pop('from_email')
                    item['to_email'] = item.pop('to_email')
                    item['message_delivery_time'] = item.pop('message_delivery_time')
                    item['size'] = item.pop('file_size')
                    item['domain'] = item.pop('domain')

                    data["ART0003"]["data"].append(item)
                    break

        json_data = data

        with open("ART0003_E-mail_Attachments.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()
            pbarroot.destroy()

    except:
        pass
