import glob, json, re

from tkinter import *
import tkinter.ttk
import tkinter as tk
import threading
from time import sleep
import os

def merge_files():
    testThread = threading.Thread(target=Callback_Start)
    testThread.start()
    testThread.join()
    
    return len(glob.glob(r"*.json"))

def Callback_Start():
    maximum = len(glob.glob(r"*.json"))
    
    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0,0)
    
    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="수집된 Json 파일들을 병합 중입니다.\n", font=('맑은 고딕', 9))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum = maximum, length=150, mode='determinate')
    pbar.pack()
    
    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)
    
    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, ))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()

def Function_Start(pbarroot, pbar):
    data = {"included" : {"artifacts": [], "events": []}}
    art_len = len(glob.glob(r"*.json"))
    
    for f in glob.glob(r"*.json"):
        sleep(0.05)
        pbar.step()
        if re.search("ART", f):
            num = re.sub(r'[^0-9]', '', f)
            data["included"]["artifacts"].append("ART"+str(num))
        else:
            num = re.sub(r'[^0-9]', '', f)
            data["included"]["events"].append("E"+str(num))
        
        with open(f, encoding="utf-8") as infile:
            data.update(json.load(infile))
    
    with open("Collect_Result_{}.json".format(art_len),'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
    
    pbarroot.destroy()