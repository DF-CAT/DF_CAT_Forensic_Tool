import os
import re
import tempfile
import sys
import pyuac
import OpenSavePidlMRU_Parser
import Prefetch_Parser
import Recent_Files_Parser
import External_Device_USB_Usage_Parser
import json_merge_files

def main():
    userprofile = ""

    with tempfile.TemporaryDirectory() as tempDir:
        if os.path.exists(tempDir):
            userprofile = resource_path(tempDir)

        OpenSaveFilesView = resource_path(r"Forensics_Tool\opensavefilesview-x64\OpenSaveFilesView")
        
        os.popen('{} /sxml {}/OpenSavePidlMRU.xml'.format(OpenSaveFilesView, userprofile)).read()

        OpenSavePidlMRU_Parser.OpenSavePidlMRU(userprofile)
        print("OpenSavePidlMRU.json 생성")
        
        pf_list = os.listdir("C:\Windows\Prefetch")
        PECmd = resource_path(r"Forensics_Tool\PECmd\PECmd.exe")
        
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
        print("Prefetch.json 생성")
        
        RecentFilesView = resource_path(r"Forensics_Tool\recentfilesview\RecentFilesView.exe")
        os.popen(r'{} /sxml {}\RecentFiles.xml'.format(RecentFilesView, userprofile)).read()

        Recent_Files_Parser.Recent_Files(userprofile)
        print("RecentFiles.json 생성")
        
        USBDeview = resource_path(r"Forensics_Tool\usbdeview-x64\USBDeview.exe")
        os.popen(r'{} /sxml {}\External_Device_USB_Usage.xml'.format(USBDeview, userprofile)).read()
        External_Device_USB_Usage_Parser.External_Device_USB_Usage(userprofile)
        print("External Device USB Usage.json 생성")
        
        # json_merge_files.merge_files()
        # print("All Artifacts.json 생성")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    # if not pyuac.isUserAdmin():
    #     pyuac.runAsAdmin()
    # else:
    #     main()

    main()