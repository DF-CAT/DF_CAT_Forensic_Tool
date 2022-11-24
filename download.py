import os
import glob
import requests
import sys
import main
from urllib.parse import urlparse
from zipfile import ZipFile

def download(downpath, usb, open_mru, prefetch, recent, lnk):
    ver = sys.maxsize > 2**32

    if ver:
        if open_mru != 0:
            url = r"https://www.nirsoft.net/utils/opensavefilesview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        if usb != 0:
            url = r"https://www.nirsoft.net/utils/usbdeview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        if prefetch != 0:
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/PECmd.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        if recent != 0:
            url = r"https://www.nirsoft.net/utils/recentfilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        if lnk != 0:
            url = r"https://www.nirsoft.net/utils/shman-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        
        for f in glob.glob(downpath+"\\"+"*.zip"):
            with ZipFile(f, 'r') as zip:
                zip.extractall(downpath)
    else:
        if open_mru != 0:
            url = r"https://www.nirsoft.net/utils/opensavefilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        if usb != 0:
            url = r"https://www.nirsoft.net/utils/usbdeview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        if prefetch != 0:
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/PECmd.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        if recent != 0:
            url = r"https://www.nirsoft.net/utils/recentfilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        if lnk != 0:
            url = r"https://www.nirsoft.net/utils/shman.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        
        for f in glob.glob(downpath+"\\"+"*.zip"):
            with ZipFile(f, 'r') as zip:
                zip.extractall(downpath)