import os
import glob
import requests
import sys
import main
from urllib.parse import urlparse
from zipfile import ZipFile


def download(downpath, usb, open_mru, prefetch, recent, lnk, shim, recycle, browser_downloads, history, jump, last,
             interfaces, shell_bags, userassist, user_accounts, outlook, bookmarks):
    ver = sys.maxsize > 2 ** 32

    if ver:
        if open_mru != 0:
            url = r"https://www.nirsoft.net/utils/opensavefilesview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if usb != 0:
            url = r"https://www.nirsoft.net/utils/usbdeview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if prefetch != 0:
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/PECmd.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if recent != 0:
            url = r"https://www.nirsoft.net/utils/recentfilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if lnk != 0:
            url = r"https://www.nirsoft.net/utils/shman-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if shim != 0:
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/AppCompatCacheParser.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if recycle != 0:
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/RBCmd.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if browser_downloads != 0:
            url = r"https://www.nirsoft.net/utils/browserdownloadsview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if history != 0:
            # url = r"https://www.nirsoft.net/utils/browsinghistoryview-x64.zip"
            url = r"https://www.nirsoft.net/utils/browsinghistoryview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if jump != 0:
            url = r"https://www.nirsoft.net/utils/jumplistsview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if last != 0:
            url = r"https://www.nirsoft.net/utils/lastactivityview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if interfaces != 0:
            url = r"https://www.nirsoft.net/utils/networkinterfacesview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if shell_bags != 0:
            url = r"https://www.nirsoft.net/utils/shellbagsview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if userassist != 0:
            url = r"https://www.nirsoft.net/utils/userassistview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if user_accounts != 0:
            url = r"https://www.nirsoft.net/utils/userprofilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if outlook != 0:
            url = r"https://www.nirsoft.net/utils/outlookattachview-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if bookmarks != 0:
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
            url = r"https://www.nirsoft.net/utils/opensavefilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if usb != 0:
            url = r"https://www.nirsoft.net/utils/usbdeview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if prefetch != 0:
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/PECmd.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if recent != 0:
            url = r"https://www.nirsoft.net/utils/recentfilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if lnk != 0:
            url = r"https://www.nirsoft.net/utils/shman.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if shim != 0:
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/AppCompatCacheParser.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if recycle != 0:
            url = r"https://f001.backblazeb2.com/file/EricZimmermanTools/RBCmd.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if browser_downloads != 0:
            url = r"https://www.nirsoft.net/utils/browserdownloadsview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if history != 0:
            url = r"https://www.nirsoft.net/utils/browsinghistoryview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if jump != 0:
            url = r"https://www.nirsoft.net/utils/jumplistsview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if last != 0:
            url = r"https://www.nirsoft.net/utils/lastactivityview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if interfaces != 0:
            url = r"https://www.nirsoft.net/utils/networkinterfacesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if shell_bags != 0:
            url = r"https://www.nirsoft.net/utils/shellbagsview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if userassist != 0:
            url = r"https://www.nirsoft.net/utils/userassistview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if user_accounts != 0:
            url = r"https://www.nirsoft.net/utils/userprofilesview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if outlook != 0:
            url = r"https://www.nirsoft.net/utils/outlookattachview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        if bookmarks != 0:
            url = r"https://www.nirsoft.net/utils/webbrowserbookmarksview.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(downpath + "\\" + file_name)
            open(down, 'wb').write(file.content)

        for f in glob.glob(downpath + "\\" + "*.zip"):
            with ZipFile(f, 'r') as zip:
                zip.extractall(downpath)