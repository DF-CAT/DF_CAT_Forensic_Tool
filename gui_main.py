import os
import threading
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
import pyuac

import main

root = Tk()

path = os.path.join(os.path.dirname(__file__), "favicon.ico")
if os.path.isfile(path):
    root.iconbitmap(path)

root.title("DF CAT Tool")
root.geometry("700x400")
root.resizable(width=False, height=False)

frame_top = tk.Frame(root)
frame_top.pack(side="top")
font = tkFont.Font(size=12)
label = Label(frame_top, text="수집할 아티팩트를 선택해 주세요\n", font=font)
label.pack(side="top")


def th():
    start_th = threading.Thread(target=Start)
    start_th.daemon = True
    start_th.start()


def Start():
    msg = messagebox.askquestion("DF CAT Tool", "아티팩트를 수집하기 위해 툴을 설치합니다.\n동의하시겠습니까?")

    if msg == "no":
        messagebox.showinfo("DF CAT Tool", "아티팩트를 수집하지 않습니다.")
    else:
        messagebox.showinfo("DF CAT Tool", "아티팩트 수집을 시작합니다.")
        button.configure(state="disabled")
        main.art_main(usb.get(), open_mru.get(), prefetch.get(), recent.get(), lnk.get(), shim.get(), recycle.get(),
                      browser_downloads.get(), history.get(), jump.get(), last.get(), interfaces.get(),
                      shell_bags.get(), userassist.get(), user_accounts.get(), outlook.get(), bookmarks.get())
        messagebox.showinfo("DF CAT Tool", "아티팩트 수집이 완료되었습니다.")
        button.configure(state="normal")


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

padding = tk.Frame(frame_bot, height=30)
padding.grid(column=1, row=7, columnspan=3)
button = Button(frame_bot, width=10, text="Start", overrelief="solid", command=th, font=font)
button.grid(column=1, row=8, sticky=tk.W)
buttonSelectAll = Button(frame_bot, width=10, text="전체선택", overrelief="solid", command=selectall, font=font)
buttonSelectAll.grid(column=1, row=9, sticky=tk.W)
buttonDeSelectAll = Button(frame_bot, width=10, text="전체취소", overrelief="solid", command=deselectall, font=font)
buttonDeSelectAll.grid(column=1, row=10, sticky=tk.W)

if __name__ == '__main__':
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        mainloop()

    # mainloop()
