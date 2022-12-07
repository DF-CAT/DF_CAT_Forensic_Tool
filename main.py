import os
import re
import sys
import tempfile

import download
import json_merge_files
from artifact_parser import ART0001_OpenSavePidlMRU_Parser, ART0009_Prefetch_Parser, ART0005_Recent_Files_Parser, \
    E0006_External_Device_USB_Usage_Parser, ART0022_LNK_Parser, ART0010_Shimcache_Parser, ART0033_Recycle_Bin_Parser, \
    ART0002_Browser_Downloads_Parser, ART0030_History_and_Download_History_Parser, ART0008_Jump_List_Parser, \
    ART0007_Last_Visited_MRU_Parser, ART0054_Network_Interfaces_Parser, ART0006_Shell_Bags_Parser, \
    ART0011_UserAssist_Parser, ART0065_User_Accounts_Parser, ART0003_Outlook_Parser, ART0060_Bookmarks_Parser


def art_main(usb, open_mru, prefetch, recent, lnk, shim, recycle, browser_downloads, history, jump, last, interfaces,
             shell_bags, userassist, user_accounts, outlook, bookmarks):
    userprofile = ""
    sys_pf = '''UPDATE|HOST|AUDIODG|AM_DELTA_PATCH|BITLOCKER|WIZARD|CALCULATOR|CHROME|CMD|SETUP|COMPAT|COMPPKGSRV
    |CONSENT|CREDENTIALUIBROKER|CSRSS|CTFMON|API|GUI|DLL|DWM|EASEOFACCESSDIALOG|EASYCONNECTMANAGER|SERVICE|EZT|FILE
    |GAME|GUP|COUNT|LOOK|HELP|MICROSOFT|MMC|MOFCOMP|MONOTIFICATIONUX|MOUSOCOREWORKER|MPC|MSCORSVW|MPSIGSTUB|MPR|VIEW
    |MSI|MSM|MSPAINTMSTEAMS|NET|NGEN|NOSSTARTER|INSTALLER|CONSOLE|RUNTIMEBROKER|TASK '''

    with tempfile.TemporaryDirectory() as tempDir:
        if os.path.exists(tempDir):
            userprofile = resource_path(tempDir)

        download.download(userprofile, usb, open_mru, prefetch, recent, lnk, shim, recycle, browser_downloads, history,
                          jump, last, interfaces, shell_bags, userassist, user_accounts, outlook, bookmarks)

        if open_mru != 0:
            OpenSaveFilesView = userprofile + r"\OpenSaveFilesView.exe"
            os.popen('{} /sxml {}/OpenSavePidlMRU.xml'.format(OpenSaveFilesView, userprofile)).read()
            ART0001_OpenSavePidlMRU_Parser.OpenSavePidlMRU(userprofile)
            print("ART0001_OpenSavePidlMRU.json 생성")

        if browser_downloads != 0:
            browser_downloads_path = userprofile + r"\BrowserDownloadsView"
            os.popen(r'{} /sjson {}\Browser_Downloads.json'.format(browser_downloads_path, userprofile)).read()
            ART0002_Browser_Downloads_Parser.Browser_Downloads(userprofile)
            print("ART0002_Browser_Downloads.json 생성")

        if outlook != 0:
            outlook_path = userprofile + r"\OutlookAttachView"
            os.popen(r'{} /sxml {}\Outlook.xml'.format(outlook_path, userprofile)).read()
            ART0003_Outlook_Parser.Outlook(userprofile)
            print("ART0003_Outlook.json 생성")

        if recent != 0:
            RecentFilesView = userprofile + r"\RecentFilesView.exe"
            os.popen(r'{} /sxml {}\RecentFiles.xml'.format(RecentFilesView, userprofile)).read()
            ART0005_Recent_Files_Parser.Recent_Files(userprofile)
            print("ART0005_Recent_Files.json 생성")

        if shell_bags != 0:
            shell_bags_path = userprofile + r"\ShellBagsView"
            os.popen(r'{} /sxml {}\Shell_Bags.xml'.format(shell_bags_path, userprofile)).read()
            ART0006_Shell_Bags_Parser.Shell_Bags(userprofile)
            print("ART0006_Shell_Bags.json 생성")

        if last != 0:
            last_path = userprofile + r"\LastActivityView"
            os.popen(r'{} /sxml {}\Last_Visited_MRU.xml'.format(last_path, userprofile)).read()
            ART0007_Last_Visited_MRU_Parser.Last_Visited_MRU(userprofile)
            print("ART0007_Last_Visited_MRU.json 생성")

        if jump != 0:
            jump_path = userprofile + r"\JumpListsView"
            os.popen(r'{} /sxml {}\Jump_Lists.xml'.format(jump_path, userprofile)).read()
            ART0008_Jump_List_Parser.Jump_Lists(userprofile)
            print("ART0008_Jump_Lists.json 생성")

        if prefetch != 0:
            cd = os.popen("%systemdrive%").read()
            pf_list = os.listdir("{}\Windows\prefetch".format(cd))
            PECmd = userprofile + r"\PECmd.exe"

            for pf in pf_list:
                if pf.endswith('.pf') and re.search(sys_pf, str(pf), re.I) is None:
                    path = r"{0}\Windows\prefetch\{1}".format(cd, pf)
                    os.popen(r'{} -f "{}" --csv {}'.format(PECmd, path, userprofile)).read()

            file_list = os.listdir(userprofile)
            file_list_py = [file for file in file_list if file.endswith(".csv")]

            path = []

            for csv in file_list_py:
                if re.compile("PECmd_Output.csv", re.I).findall(csv):
                    path.append(userprofile + "/" + csv)

            ART0009_Prefetch_Parser.Prefetch(path)
            print("ART0009_Prefetch.json 생성")

        if shim != 0:
            shim_path = userprofile + r"\AppCompatCacheParser.exe"
            os.popen(r'{} --csv {} --csvf Shimcache.csv'.format(shim_path, userprofile)).read()
            ART0010_Shimcache_Parser.Shimcache(userprofile)
            print("ART0010_ShimCache.json 생성")

        if userassist != 0:
            userassist_path = userprofile + r"\UserAssistView"
            os.popen(r'{} /sxml {}\UserAssist.xml'.format(userassist_path, userprofile)).read()
            ART0011_UserAssist_Parser.UserAssist(userprofile)
            print("ART0011_UserAssist.json 생성")

        if lnk != 0:
            lnk_path = userprofile + r"\shman"
            os.popen(r'{} /stab {}\Shortcut_LNK_Files.txt'.format(lnk_path, userprofile)).read()
            ART0022_LNK_Parser.Shortcut_LNK_Files(userprofile)
            print("ART0022_Shortcut_LNK_Files.json 생성")

        if history != 0:
            history_path = userprofile + r"\BrowsingHistoryView"
            os.popen(r'{} /scomma {}\History_and_Download_History.csv'.format(history_path, userprofile)).read()
            ART0030_History_and_Download_History_Parser.History_and_Download_History(userprofile)
            print("ART0030_History_and_Download_History.json 생성")

        if recycle != 0:
            recycle_path = userprofile + r"\RBCmd.exe"
            os.popen(r'{} -d %systemdrive%\$Recycle.Bin --csv {} --csvf Recycle_Bin.csv'.format(recycle_path,
                                                                                                userprofile)).read()
            ART0033_Recycle_Bin_Parser.Recycle_Bin(userprofile)
            print("ART0033_Recycle_Bin.json 생성")

        if interfaces != 0:
            interfaces_path = userprofile + r"\NetworkInterfacesView"
            os.popen(r'{} /sxml {}\Network_Interfaces.xml'.format(interfaces_path, userprofile)).read()
            ART0054_Network_Interfaces_Parser.Network_Interfaces(userprofile)
            print("ART0054_Network_Interfaces.json 생성")

        if bookmarks != 0:
            bookmarks_path = userprofile + r"\WebBrowserBookmarksView"
            os.popen(r'{} /sjson {}\Bookmarks.json'.format(bookmarks_path, userprofile)).read()
            ART0060_Bookmarks_Parser.Bookmarks(userprofile)
            print("ART0060_Bookmarks.json 생성")

        if user_accounts != 0:
            user_accounts_path = userprofile + r"\UserProfilesView"
            os.popen(r'{} /sxml {}\User_Accounts.xml'.format(user_accounts_path, userprofile)).read()
            ART0065_User_Accounts_Parser.User_Accounts(userprofile)
            print("ART0065_User_Accounts.json 생성")

        if usb != 0:
            USBDeview = userprofile + r"\USBDeview.exe"
            os.popen(r'{} /sxml {}\External_Device_USB_Usage.xml'.format(USBDeview, userprofile)).read()
            E0006_External_Device_USB_Usage_Parser.External_Device_USB_Usage(userprofile)
            print("E0006_External_Device_USB_Usage.json 생성")

        art_len = json_merge_files.merge_files()
        print("Collect_Result_{}.json 생성".format(art_len))


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
