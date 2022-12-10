import os
import glob
import requests
import sys
import main
from urllib.parse import urlparse
from zipfile import ZipFile

from tkinter import *
import tkinter.ttk
import tkinter as tk
import threading
from time import sleep

def download(downpath, usb, open_mru, prefetch, recent, lnk, shim, recycle, browser_downloads, history,
                          jump, last, interfaces, shell_bags, userassist, user_accounts, outlook, bookmarks):
    testThread = threading.Thread(target=Callback_Start, args=(downpath, usb, open_mru, prefetch, recent, lnk, shim, recycle, browser_downloads, history,
                          jump, last, interfaces, shell_bags, userassist, user_accounts, outlook, bookmarks, ))
    testThread.start()
    testThread.join()

def Callback_Start(downpath, usb, open_mru, prefetch, recent, lnk, shim, recycle, browser_downloads, history,
                          jump, last, interfaces, shell_bags, userassist, user_accounts, outlook, bookmarks):
    maximum = 100
    
    pbarroot = Tk()
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    if os.path.isfile(path):
        pbarroot.iconbitmap(path)
    pbarroot.title('DF CAT Tool')
    pbarroot.geometry("235x85")
    pbarroot.resizable(0,0)
    
    paddingTop = Frame(pbarroot, height=10, width=235)
    paddingTop.pack(side="top", fill="both", expand=True)
    label = Label(pbarroot, text="\n", font=('맑은 고딕', 9))
    label.pack(side="top")

    pbar = tkinter.ttk.Progressbar(pbarroot, orient=HORIZONTAL, maximum = maximum, length=150, mode='determinate')
    pbar.pack()
    
    paddingBottom = tk.Frame(pbarroot, height=10)
    paddingBottom.pack(side="bottom", fill="x", expand=True)

    tThread = threading.Thread(target=Function_Start, args=(label, pbarroot, pbar, downpath, usb, open_mru, prefetch, recent, lnk, shim, recycle, browser_downloads, history,
                          jump, last, interfaces, shell_bags, userassist, user_accounts, outlook, bookmarks, ))
    tThread.setDaemon(True)
    tThread.start()
    pbarroot.mainloop()

def Function_Start(label, pbarroot, pbar, downpath, usb, open_mru, prefetch, recent, lnk, shim, recycle, browser_downloads, history,
                          jump, last, interfaces, shell_bags, userassist, user_accounts, outlook, bookmarks):
    ver = sys.maxsize > 2 ** 32

    i = usb + open_mru + prefetch + recent + lnk + shim + recycle + browser_downloads + history +\
        jump + last + interfaces + shell_bags + userassist + user_accounts + outlook + bookmarks
    
    i = 100 / i
    
    if ver:
        if open_mru != 0:
            label["text"] = "opensavefilesview-x64 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/opensavefilesview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if usb != 0:
            label["text"] = "usbdeview-x64 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/usbdeview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if prefetch != 0:
            label["text"] = "winprefetchview-x64 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/winprefetchview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if recent != 0:
            label["text"] = "recentfilesview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/recentfilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if lnk != 0:
            label["text"] = "shman-x64 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/shman-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if shim != 0:
            label["text"] = "AppCompatCacheParser 다운로드 중\n"
            pbar.step(i)
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/AppCompatCacheParser.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if recycle != 0:
            label["text"] = "RBCmd 다운로드 중\n"
            pbar.step(i)
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/RBCmd.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if browser_downloads != 0:
            label["text"] = "browserdownloadsview-x64 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/browserdownloadsview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if history != 0:
            label["text"] = "browsinghistoryview 다운로드 중\n"
            pbar.step(i)
            # url = r"https://www.nirsoft.net/utils/browsinghistoryview-x64.zip"
            url = r"https://www.nirsoft.net/utils/browsinghistoryview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if jump != 0:
            label["text"] = "jumplistsview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/jumplistsview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if last != 0:
            label["text"] = "lastactivityview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/lastactivityview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if interfaces != 0:
            label["text"] = "networkinterfacesview-x64 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/networkinterfacesview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if shell_bags != 0:
            label["text"] = "shellbagsview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/shellbagsview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if userassist != 0:
            label["text"] = "userassistview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/userassistview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if user_accounts != 0:
            label["text"] = "userprofilesview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/userprofilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if outlook != 0:
            label["text"] = "outlookattachview-x64 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/outlookattachview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if bookmarks != 0:
            label["text"] = "webbrowserbookmarksview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/webbrowserbookmarksview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        for f in glob.glob(downpath + "\\" + "*.zip"):
            with ZipFile(f, 'r') as zip:
                zip.extractall(downpath)
        
    else:
        if open_mru != 0:
            label["text"] = "opensavefilesview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/opensavefilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if usb != 0:
            label["text"] = "usbdeview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/usbdeview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if prefetch != 0:
            label["text"] = "winprefetchview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/winprefetchview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if recent != 0:
            label["text"] = "recentfilesview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/recentfilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if lnk != 0:
            label["text"] = "shman 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/shman.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if shim != 0:
            label["text"] = "AppCompatCacheParser 다운로드 중\n"
            pbar.step(i)
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/AppCompatCacheParser.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if recycle != 0:
            label["text"] = "RBCmd 다운로드 중\n"
            pbar.step(i)
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/RBCmd.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if browser_downloads != 0:
            label["text"] = "browserdownloadsview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/browserdownloadsview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if history != 0:
            label["text"] = "browsinghistoryview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/browsinghistoryview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if jump != 0:
            label["text"] = "jumplistsview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/jumplistsview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if last != 0:
            label["text"] = "lastactivityview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/lastactivityview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if interfaces != 0:
            label["text"] = "networkinterfacesview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/networkinterfacesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if shell_bags != 0:
            label["text"] = "shellbagsview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/shellbagsview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if userassist != 0:
            label["text"] = "userassistview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/userassistview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if user_accounts != 0:
            label["text"] = "userprofilesview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/userprofilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if outlook != 0:
            label["text"] = "outlookattachview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/outlookattachview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if bookmarks != 0:
            label["text"] = "webbrowserbookmarksview 다운로드 중\n"
            pbar.step(i)
            url = r"https://www.nirsoft.net/utils/webbrowserbookmarksview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        for f in glob.glob(downpath + "\\" + "*.zip"):
            with ZipFile(f, 'r') as zip:
                zip.extractall(downpath)
    
    pbarroot.destroy()