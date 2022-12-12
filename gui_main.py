import os
import threading
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyuac

import main

root = Tk()

path = os.path.join(os.path.dirname(__file__), "favicon.ico")
if os.path.isfile(path):
    root.iconbitmap(path)

root.title("DF CAT Tool")
root.geometry("650x350")
root.resizable(width=False, height=False)

paddingTop = Frame(root, height=20, width=700)
paddingTop.pack(side="top", fill="both", expand=True)
frame_top = tk.Frame(root)
frame_top.pack(side="top")
font = tkFont.Font(size=12)
label = Label(frame_top, text="수집할 아티팩트를 선택해 주세요\n", font=font)
label.pack(side="top")

dir_path = None

def th():
    start_th = threading.Thread(target=Start)
    start_th.daemon = True
    start_th.start()


def Start():
    if dir_path is not None:
        msg = messagebox.askquestion("DF CAT Tool", "아티팩트를 수집하기 위해 툴을 설치합니다.\n동의하시겠습니까?")

        if msg == "no":
            messagebox.showinfo("DF CAT Tool", "아티팩트를 수집하지 않습니다.")
        else:
            messagebox.showinfo("DF CAT Tool", "아티팩트 수집을 시작합니다.")
            button.configure(state="disabled")

            if Json.get() != 1 and CSV.get() != 1:
                messagebox.showinfo("DF CAT Tool", "추출할 형식을 체크해주세요")
            else:
                main.art_main(usb.get(), open_mru.get(), prefetch.get(), recent.get(), lnk.get(), shim.get(), recycle.get(),
                          browser_downloads.get(), history.get(), jump.get(), last.get(), interfaces.get(),
                          shell_bags.get(), userassist.get(), user_accounts.get(), outlook.get(), bookmarks.get(), Json.get(), CSV.get(),dir_path)
                messagebox.showinfo("DF CAT Tool", "아티팩트 수집이 완료되었습니다.")

            button.configure(state="normal")
    else:
        messagebox.showinfo("DF CAT Tool", "경로를 지정해주세요")


def selectall():
    bt1.select()
    bt2.select()
    bt3.select()
    bt4.select()
    bt5.select()
    bt6.select()
    bt7.select()
    bt8.select()
    bt9.select()
    bt10.select()
    bt11.select()
    bt12.select()
    bt13.select()
    bt14.select()
    bt15.select()
    bt16.select()
    bt17.select()

def deselectall():
    bt1.deselect()
    bt2.deselect()
    bt3.deselect()
    bt4.deselect()
    bt5.deselect()
    bt6.deselect()
    bt7.deselect()
    bt8.deselect()
    bt9.deselect()
    bt10.deselect()
    bt11.deselect()
    bt12.deselect()
    bt13.deselect()
    bt14.deselect()
    bt15.deselect()
    bt16.deselect()
    bt17.deselect()

def select_dir_path():
    global dir_path
    dir_path = filedialog.askdirectory(parent=root, initialdir="/", title='DF_CAT_Tool')
    text_path.configure(state='normal')
    text_path.insert(1.0, dir_path)
    text_path.configure(state='disabled')

usb = IntVar()
open_mru = IntVar()
prefetch = IntVar()
recent = IntVar()
lnk = IntVar()
shim = IntVar()
recycle = IntVar()
browser_downloads = IntVar()
history = IntVar()
jump = IntVar()
last = IntVar()
interfaces = IntVar()
shell_bags = IntVar()
userassist = IntVar()
user_accounts = IntVar()
outlook = IntVar()
bookmarks = IntVar()

frame_bot = tk.Frame(root)
frame_bot.pack(side="top")

bt1 = Checkbutton(frame_bot, text="External Device/USB Usage", variable=usb, font=font)
bt2 = Checkbutton(frame_bot, text="Open/Save MRU", variable=open_mru, font=font)
bt3 = Checkbutton(frame_bot, text="Prefetch", variable=prefetch, font=font)
bt4 = Checkbutton(frame_bot, text="Recent Files", variable=recent, font=font)
bt5 = Checkbutton(frame_bot, text="Shortcut (LNK) Files", variable=lnk, font=font)
bt6 = Checkbutton(frame_bot, text="Shimcache", variable=shim, font=font)
bt7 = Checkbutton(frame_bot, text="Recycle Bin", variable=recycle, font=font)
bt8 = Checkbutton(frame_bot, text="Browser Downloads", variable=browser_downloads, font=font)
bt9 = Checkbutton(frame_bot, text="Web History", variable=history, font=font)
bt10 = Checkbutton(frame_bot, text="Jump Lists", variable=jump, font=font)
bt11 = Checkbutton(frame_bot, text="Last Visited MRU", variable=last, font=font)
bt12 = Checkbutton(frame_bot, text="Network Interfaces", variable=interfaces, font=font)
bt13 = Checkbutton(frame_bot, text="Shell Bags", variable=shell_bags, font=font)
bt14 = Checkbutton(frame_bot, text="UserAssist", variable=userassist, font=font)
bt15 = Checkbutton(frame_bot, text="User Accounts", variable=user_accounts, font=font)
bt16 = Checkbutton(frame_bot, text="E-mail Attachments", variable=outlook, font=font)
bt17 = Checkbutton(frame_bot, text="Bookmarks", variable=bookmarks, font=font)

bt1.grid(column=0, row=1, sticky=tk.W)
bt2.grid(column=0, row=2, sticky=tk.W)
bt3.grid(column=0, row=3, sticky=tk.W)
bt4.grid(column=0, row=4, sticky=tk.W)
bt5.grid(column=0, row=5, sticky=tk.W)
bt6.grid(column=0, row=6, sticky=tk.W)
bt7.grid(column=1, row=1, sticky=tk.W)
bt8.grid(column=1, row=2, sticky=tk.W)
bt9.grid(column=1, row=3, sticky=tk.W)
bt10.grid(column=1, row=4, sticky=tk.W)
bt11.grid(column=1, row=5, sticky=tk.W)
bt12.grid(column=1, row=6, sticky=tk.W)
bt13.grid(column=2, row=1, sticky=tk.W)
bt14.grid(column=2, row=2, sticky=tk.W)
bt15.grid(column=2, row=3, sticky=tk.W)
bt16.grid(column=2, row=4, sticky=tk.W)
bt17.grid(column=2, row=5, sticky=tk.W)


frame_btn = tk.Frame(root)
frame_btn.pack(side="top")

padding = tk.Frame(frame_btn, height=10)
padding.pack(side="top", fill="both", expand=True)
buttonSelectAll = Button(frame_btn, width=10, text="전체선택", overrelief="solid", command=selectall, font=font)
buttonSelectAll.pack(side="left")
label0 = Label(frame_btn)
label0.pack(side="left")
buttonDeSelectAll = Button(frame_btn, width=10, text="전체취소", overrelief="solid", command=deselectall, font=font)
buttonDeSelectAll.pack(side="left")
label1 = Label(frame_btn)
label1.pack(side="left")
button = Button(frame_btn, width=10, text="Start", overrelief="solid", command=th, font=font)
button.pack(side="left")
label4 = Label(frame_btn)
label4.pack(side="left")

Json = IntVar()
CSV = IntVar()

Json_bt = Checkbutton(frame_btn, text="Export Json", variable=Json, font=("", 10))
CSV_bt = Checkbutton(frame_btn, text="Export CSV", variable=CSV, font=("", 10))

Json_bt.pack(side="top")
CSV_bt.pack(side="top")

frame_path = tk.Frame(root)
frame_path.pack(side="top")

padding = tk.Frame(frame_path, height=10)
padding.pack(side="top", fill="both", expand=True)

path_bt = Button(frame_path, width=10, text="폴더 선택", overrelief="solid", command=select_dir_path, font=font)
path_bt.pack(side="left")
label3 = Label(frame_path)
label3.pack(side="left")
text_path = Text(frame_path, width = 45, height = 1, relief = "groove", font=("맑은 고딕", 10), wrap="none", pady=5)
text_path.configure(state='disabled')
text_path.pack(side="left")

paddingBottom = tk.Frame(root, height=10)
paddingBottom.pack(side="bottom", fill="x", expand=True)


if __name__ == '__main__':
    # if not pyuac.isUserAdmin():
    #     pyuac.runAsAdmin()
    # else:
    #     mainloop()

    mainloop()