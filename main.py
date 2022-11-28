import os, re, tempfile, sys
import OpenSavePidlMRU_Parser
import Prefetch_Parser
import Recent_Files_Parser
import External_Device_USB_Usage_Parser
import json_merge_files
import LNK_Parser
import download

import glob
import requests
import sys
import main
from urllib.parse import urlparse
from zipfile import ZipFile

def art_main(usb, open_mru, prefetch, recent, lnk):
    userprofile = ""
    sys_pf = '''UPDATE|HOST|AUDIODG|AM_DELTA_PATCH|BITLOCKER|WIZARD|CALCULATOR|CHROME|CMD|SETUP|COMPAT|COMPPKGSRV|CONSENT|CREDENTIALUIBROKER|CSRSS|CTFMON|API|GUI|DLL|DWM|EASEOFACCESSDIALOG|EASYCONNECTMANAGER|SERVICE|EZT|FILE|GAME|GUP|COUNT|LOOK|HELP|MICROSOFT|MMC|MOFCOMP|MONOTIFICATIONUX|MOUSOCOREWORKER|MPC|MSCORSVW|MPSIGSTUB|MPR|VIEW|MSI|MSM|MSPAINTMSTEAMS|NET|NGEN|NOSSTARTER|INSTALLER|CONSOLE|RUNTIMEBROKER|TASK'''
    
    with tempfile.TemporaryDirectory() as tempDir:
        if os.path.exists(tempDir):
            userprofile = resource_path(tempDir)
    
        # download.download(userprofile, usb, open_mru, prefetch, recent, lnk)

        if open_mru != 0:
            OpenSaveFilesView = userprofile+r"\OpenSaveFilesView.exe"

            os.popen('{} /sxml {}/OpenSavePidlMRU.xml'.format(OpenSaveFilesView, userprofile)).read()

            OpenSavePidlMRU_Parser.OpenSavePidlMRU(userprofile)
            print("ART0001_OpenSavePidlMRU.json 생성")

        if prefetch != 0:
            pf_list = os.listdir("C:\Windows\Prefetch")
            PECmd = userprofile+r"\PECmd.exe"

            for pf in pf_list:
                if pf.endswith('.pf') and len(re.compile(sys_pf, re.I).findall(pf)) == 0:
                    path = r"C:\Windows\Prefetch\{}".format(pf)
                    os.popen(r'{} -f "{}" --csv {}'.format(PECmd, path, userprofile)).read()

            file_list = os.listdir(userprofile)
            file_list_py = [file for file in file_list if file.endswith(".csv")]

            path = []

            for csv in file_list_py:
                if re.compile("PECmd_Output.csv", re.I).findall(csv):
                    path.append(userprofile + "/" + csv)

            Prefetch_Parser.Prefetch(path)
            print("ART0010_Prefetch.json 생성")

        if recent != 0:
            RecentFilesView = userprofile+r"\RecentFilesView.exe"
            os.popen(r'{} /sxml {}\RecentFiles.xml'.format(RecentFilesView, userprofile)).read()

            Recent_Files_Parser.Recent_Files(userprofile)
            print("ART0006_Recent_Files.json 생성")

        if usb != 0:
            USBDeview = userprofile+r"\USBDeview.exe"
            os.popen(r'{} /sxml {}\External_Device_USB_Usage.xml'.format(USBDeview, userprofile)).read()
            External_Device_USB_Usage_Parser.External_Device_USB_Usage(userprofile)
            print("E0006_External_Device_USB_Usage.json 생성")

        if lnk != 0:
            url = r"https://www.nirsoft.net/utils/shman-x64.zip"
            parsed_file = urlparse(url)
            file_name = os.path.basename(parsed_file.path)
            file = requests.get(url)
            down = main.resource_path(userprofile +"\\"+  file_name)
            open(down, 'wb').write(file.content)
        
        
            for f in glob.glob(userprofile+"\\"+"*.zip"):
                with ZipFile(f, 'r') as zip:
                    zip.extractall(userprofile)
            
            lnk = userprofile+r"\shman"
            os.popen(r'{} /sxml {}\Shortcut_LNK_Files.xml'.format(lnk, userprofile)).read()
            LNK_Parser.Shortcut_LNK_Files(userprofile)
            print("ART0022_Shortcut_LNK_Files.json 생성")

        art_len = json_merge_files.merge_files()
        print("Collect_Result_{}.json 생성".format(art_len))
    
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

art_main(0, 0, 0, 0, 1)