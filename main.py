import os, re, tempfile, sys
import OpenSavePidlMRU_Parser
import Prefetch_Parser
import Recent_Files_Parser
import External_Device_USB_Usage_Parser
import json_merge_files
import LNK_Parser
import download

def art_main(usb, open_mru, prefetch, recent, lnk, shim, recycle, browser_downloads, history, jump, last, interfaces, shell_bags, userassist, user_accounts, outlook, bookmarks):
    userprofile = ""
    sys_pf = '''UPDATE|HOST|AUDIODG|AM_DELTA_PATCH|BITLOCKER|WIZARD|CALCULATOR|CHROME|CMD|SETUP|COMPAT|COMPPKGSRV|CONSENT|CREDENTIALUIBROKER|CSRSS|CTFMON|API|GUI|DLL|DWM|EASEOFACCESSDIALOG|EASYCONNECTMANAGER|SERVICE|EZT|FILE|GAME|GUP|COUNT|LOOK|HELP|MICROSOFT|MMC|MOFCOMP|MONOTIFICATIONUX|MOUSOCOREWORKER|MPC|MSCORSVW|MPSIGSTUB|MPR|VIEW|MSI|MSM|MSPAINTMSTEAMS|NET|NGEN|NOSSTARTER|INSTALLER|CONSOLE|RUNTIMEBROKER|TASK'''
    
    with tempfile.TemporaryDirectory() as tempDir:
        if os.path.exists(tempDir):
            userprofile = resource_path(tempDir)
    
        download.download(userprofile, usb, open_mru, prefetch, recent, lnk, shim, recycle, browser_downloads, history, jump, last, interfaces, shell_bags, userassist, user_accounts, outlook, bookmarks)

        if open_mru != 0:
            OpenSaveFilesView = userprofile+r"\OpenSaveFilesView.exe"

            os.system('{} /sxml {}/OpenSavePidlMRU.xml'.format(OpenSaveFilesView, userprofile))

            OpenSavePidlMRU_Parser.OpenSavePidlMRU(userprofile)
            print("ART0001_OpenSavePidlMRU.json 생성")

        if prefetch != 0:
            cd = os.popen("cd").read()
            pf_list = os.listdir("{}:\Windows\prefetch".format(cd.split(":")[0]))
            PECmd = userprofile+r"\PECmd.exe"

            for pf in pf_list:
                if pf.endswith('.pf') and len(re.compile(sys_pf, re.I).findall(pf)) == 0:
                    path = r"{0}:\Windows\prefetch\{1}".format(cd.split(":")[0], pf)
                    os.system(r'{} -f "{}" --csv {}'.format(PECmd, path, userprofile))

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
            os.system(r'{} /sxml {}\RecentFiles.xml'.format(RecentFilesView, userprofile))

            Recent_Files_Parser.Recent_Files(userprofile)
            print("ART0006_Recent_Files.json 생성")

        if usb != 0:
            USBDeview = userprofile+r"\USBDeview.exe"
            os.system(r'{} /sxml {}\External_Device_USB_Usage.xml'.format(USBDeview, userprofile))
            External_Device_USB_Usage_Parser.External_Device_USB_Usage(userprofile)
            print("E0006_External_Device_USB_Usage.json 생성")

        if lnk != 0:
            lnk = userprofile+r"\shman"
            os.system(r'{} /stab {}\Shortcut_LNK_Files.txt'.format(lnk, userprofile))
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
