import os, re, tempfile, sys
import OpenSavePidlMRU_Parser
import Prefetch_Parser
import Recent_Files_Parser
import External_Device_USB_Usage_Parser
import json_merge_files
import LNK_Parser
import download

def art_main(usb, open_mru, prefetch, recent, lnk):
    userprofile = ""

    with tempfile.TemporaryDirectory() as tempDir:
        if os.path.exists(tempDir):
            userprofile = resource_path(tempDir)
        
        downpath = resource_path(userprofile+"\Forensics_Tool")
        download.download(downpath, usb, open_mru, prefetch, recent, lnk)
        
        if open_mru != 0:
            OpenSaveFilesView = downpath+"\OpenSaveFilesView"

            os.popen('{} /sxml {}/OpenSavePidlMRU.xml'.format(OpenSaveFilesView, userprofile)).read()

            OpenSavePidlMRU_Parser.OpenSavePidlMRU(userprofile)
            print("ART0001_OpenSavePidlMRU.json 생성")
        
        if prefetch != 0:
            pf_list = os.listdir("C:\Windows\Prefetch")
            PECmd = downpath+"\PECmd.exe"

            for pf in pf_list:
                if pf.endswith('.pf'):
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
            RecentFilesView = downpath+"\RecentFilesView.exe"
            os.popen(r'{} /sxml {}\RecentFiles.xml'.format(RecentFilesView, userprofile)).read()

            Recent_Files_Parser.Recent_Files(userprofile)
            print("ART0006_Recent_Files.json 생성")
        
        if usb != 0:
            USBDeview = downpath+"\USBDeview.exe"
            os.popen(r'{} /sxml {}\External_Device_USB_Usage.xml'.format(USBDeview, userprofile)).read()
            External_Device_USB_Usage_Parser.External_Device_USB_Usage(userprofile)
            print("E0006_External_Device_USB_Usage.json 생성")
        
        if lnk != 0:
            lnk = downpath+"\shman.exe"
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