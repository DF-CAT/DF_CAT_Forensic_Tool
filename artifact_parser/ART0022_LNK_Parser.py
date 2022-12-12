import json
import os
import threading
import tkinter as tk
import tkinter.ttk
from time import sleep
from tkinter import *


def Shortcut_LNK_Files(userprofile):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile,))
    testThread.start()
    testThread.join()


def Callback_Start(userprofile):
    with open(r"{}\Shortcut_LNK_Files.txt".format(userprofile)) as txt_file:
        result = txt_file.readlines()
    maximum = len(result)

    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0, 0)

    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="Shortcut LNK Files 수집 중\n", font=('맑은 고딕', 11))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum=maximum, length=150, mode='determinate')
    pbar.pack()

    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, result,))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()


def Function_Start(pbarroot, pbar, result):
    data = {"ART0022": {"name": "Shortcut_LNK_Files", "isEvent": False, "data": []}}

    try:
        for i in result:
            sleep(0.001)
            pbar.step()
            re = i.split('\t')
            for key in re:
                if key is not None:
                    if re[9] is not None:
                        data["ART0022"]["data"].append(
                            {"name": re[0], "modified_time": re[9], "path": re[11], "real_path": re[2],
                             "timeline_items": [{"name": "modified_time", "start_time": re[9], "end_time": re[9]}]})
                    else:
                        data["ART0022"]["data"].append(
                            {"name": re[0], "modified_time": re[9], "path": re[11], "real_path": re[2],
                             "timeline_items": []})
                    break

        json_data = data

        with open("ART0022_Shortcut_LNK_Files.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()
            pbarroot.destroy()

    except:
        pass
