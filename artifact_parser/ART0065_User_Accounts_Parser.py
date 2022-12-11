import json
import os
import threading
import tkinter as tk
import tkinter.ttk
from time import sleep
from tkinter import *

import xmltodict


def User_Accounts(userprofile):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile,))
    testThread.start()
    testThread.join()


def Callback_Start(userprofile):
    with open("{}\\User_Accounts.xml".format(userprofile), encoding='utf-16') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    maximum = len(data_dict["profiles_list"]["item"])

    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0, 0)

    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="User Accounts 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum=maximum, length=150, mode='determinate')
    pbar.pack()

    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, data_dict,))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()


def Function_Start(pbarroot, pbar, data_dict):
    data = {"ART0065": {"name": "User_Accounts", "isEvent": False, "data": [], "timeline_items": []}}

    try:
        for item in data_dict["profiles_list"]["item"]:
            sleep(0.1)
            pbar.step()
            itemd = item.copy()
            Ndel = ["user_name", "profile_path", "folder_created_time", "registry_modified_time", "logon_time"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            for key in item:
                if item[key] is not None:
                    data["ART0065"]["data"].append(item)
                    break

            if item["folder_created_time"] is not None:
                data["ART0065"]["timeline_items"].append(
                    {"name": "folder_created_time", "start_time": item["folder_created_time"],
                     "end_time": item["folder_created_time"]})
                data["ART0065"]["timeline_items"].append(
                    {"name": "registry_modified_time", "start_time": item["registry_modified_time"],
                     "end_time": item["registry_modified_time"]})
                data["ART0065"]["timeline_items"].append(
                    {"name": "logon_time", "start_time": item["logon_time"], "end_time": item["logon_time"]})

        json_data = data

        with open("ART0065_User_Accounts.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()
            pbarroot.destroy()

    except:
        pass
