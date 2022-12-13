import glob, json, re
import pandas as pd

from tkinter import *
import tkinter.ttk
import tkinter as tk
import threading
from time import sleep
import os

def merge_files(json_path, CSV, csv_path):
    testThread = threading.Thread(target=Callback_Start, args=(json_path, CSV, csv_path, ))
    testThread.start()
    testThread.join()
    
    if CSV != 0:
        return len(glob.glob(csv_path + r"/" + r"*.csv"))
    else:
        return len(glob.glob(json_path + r"/" + r"*.json"))

def Callback_Start(json_path, CSV, csv_path):
    try:
        maximum = len(glob.glob(json_path + r"/" + r"*.json"))
    except:
        maximum = len(glob.glob(csv_path + r"/" + r"*.csv"))
    
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
    
    tThread = threading.Thread(target=Function_Start, args=(pbarroot, pbar, json_path, CSV, csv_path, ))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()

def Function_Start(pbarroot, pbar, json_path, CSV, csv_path):
    if json_path is not None:
        data = {"version": "1.0.4", "included" : {"version": "1.0.4","artifacts": [], "events": []}}
        art_len = len(glob.glob(json_path + r"/" + r"*.json"))

        for f in glob.glob(json_path + r"/" + r"*.json"):
            sleep(0.05)
            pbar.step()
            file = os.path.basename(f)
            if re.search("ART", file):
                num = re.sub(r'[^0-9]', '', file)
                data["included"]["artifacts"].append("ART"+str(num))
            else:
                num = re.sub(r'[^0-9]', '', file)
                data["included"]["events"].append("E"+str(num))

            with open(f, encoding="utf-8") as infile:
                jf = json.load(infile)
                del jf["version"]
                data.update(jf)

        with open(r"{0}/Collect_Result_{1}.json".format(json_path, art_len),'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)
    
    if CSV != 0:
        art_len = len(glob.glob(csv_path + r"/" + r"*.csv"))
        file_format = ".csv" # .csv .xlsx
        file_list = glob.glob(f"{csv_path}/*{file_format}")

        writer=pd.ExcelWriter(r'{0}\Collect_Result_{1}.xlsx'.format(csv_path, art_len), engine='openpyxl')

        for csv in file_list:
            sleep(0.05)
            pbar.step()
            name = os.path.splitext(os.path.basename(csv))
            file_df = pd.read_csv(csv, encoding='ANSI')
            file_df.to_excel(writer, sheet_name=name[0], index=False)

        writer.save()
    
    pbarroot.destroy()