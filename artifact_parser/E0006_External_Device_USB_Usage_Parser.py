import json
import os
import threading
import tkinter as tk
import tkinter.ttk
from time import sleep
from tkinter import *

import xmltodict


def External_Device_USB_Usage(userprofile):
    testThread = threading.Thread(target=Callback_Start, args=(userprofile,))
    testThread.start()
    testThread.join()


def Callback_Start(userprofile):
    with open("{}\\External_Device_USB_Usage.xml".format(userprofile), encoding='euc-kr') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    maximum = len(data_dict["usb_devices_list"]["item"])

    pbarroot = Tk()

    path = os.path.join(os.path.dirname(__file__), "../../../../Downloads/artifact_parser/favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)

    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0, 0)

    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="External Device USB Usage 수집 중\n", font=('맑은 고딕', 9))
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
    data = {"E0006": {"name": "External_Device_USB_Usage", "isEvent": True, "data": [], "timeline_items": []}}

    try:
        for item in data_dict["usb_devices_list"]["item"]:
            sleep(0.1)
            pbar.step()
            itemd = item.copy()

            Ndel = ["description", "device_type", "serial_number", "registry_time_1", "registry_time_2",
                    "driver_description", "instance_id", "capabilities", "connect_time", "disconnect_time"]

            for key in itemd.keys():
                num = 0
                for n in Ndel:
                    if key != n:
                        num += 1
                    if num == len(Ndel):
                        del item[key]

            item['created_time'] = item.pop('registry_time_1')
            item['last_plug_unplug_time'] = item.pop('registry_time_2')

            for key in item:
                if item[key] is not None:
                    data["E0006"]["data"].append(item)
                    break

            if item["connect_time"] is None and item["disconnect_time"] is None:
                continue

            if item["connect_time"] is None:
                item["connect_time"] = item["disconnect_time"]

            elif item["disconnect_time"] is None:
                item["disconnect_time"] = item["connect_time"]

            data["E0006"]["timeline_items"].append(
                {"name": "description", "start_time": item["connect_time"], "end_time": item["disconnect_time"]})

        json_data = data

        with open("E0006_External_Device_USB_Usage.json", "w", encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

            json_file.close()
            pbarroot.destroy()

    except:
        pass
