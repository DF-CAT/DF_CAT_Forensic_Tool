from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import main
import threading
import os
import pyuac

root = Tk()

path = os.path.join(os.path.dirname(__file__), "favicon.ico")
if os.path.isfile(path):
    root.iconbitmap(path)

root.title("DF CAT Tool")
root.geometry("300x400")
root.resizable(width=False, height=False)

frame_top = tk.Frame(root)
frame_top.pack(side="top")
font = tkFont.Font(size=12)
label = Label(frame_top, text="수집할 아티팩트를 선택해 주세요\n", font=font)
label.pack(side="top")

def th():
    th = threading.Thread(target=Start)
    th.daemon = True
    th.start()

def Start():
    msg = messagebox.askquestion("DF CAT Tool", "아티팩트를 수집하기 위해 툴을 설치합니다.\n동의하시겠습니까?")
    
    if msg == "no":
        messagebox.showinfo("DF CAT Tool", "아티팩트를 수집하지 않습니다.")
    else:
        messagebox.showinfo("DF CAT Tool", "아티팩트 수집을 시작합니다.")
        main.art_main(usb.get(), open_mru.get(), prefetch.get(), recent.get(), lnk.get())
        messagebox.showinfo("DF CAT Tool", "아티팩트 수집이 완료되었습니다.")

def selectall():
    bt1.select()
    bt2.select()
    bt3.select()
    bt4.select()
    bt5.select()

def deselectall():
    bt1.deselect()
    bt2.deselect()
    bt3.deselect()
    bt4.deselect()
    bt5.deselect()

usb = IntVar()
open_mru = IntVar()
prefetch = IntVar()
recent = IntVar()
lnk = IntVar()

frame_bot = tk.Frame(root)
frame_bot.pack(side="top")

bt1 = Checkbutton(frame_bot, text="External Device/USB Usage", variable=usb, font=font)
bt2 = Checkbutton(frame_bot, text="Open/Save MRU", variable=open_mru, font=font)
bt3 = Checkbutton(frame_bot, text="Prefetch", variable=prefetch, font=font)
bt4 = Checkbutton(frame_bot, text="Recent Files", variable=recent, font=font)
bt5 = Checkbutton(frame_bot, text="Shortcut (LNK) Files", variable=lnk, font=font)

bt1.grid(column=0, row=1, sticky=tk.W)
bt2.grid(column=0, row=2, sticky=tk.W)
bt3.grid(column=0, row=3, sticky=tk.W)
bt4.grid(column=0, row=4, sticky=tk.W)
bt5.grid(column=0, row=5, sticky=tk.W)

button = Button(frame_bot, width=10, text="Start", overrelief="solid", command=th, font=font)
button.grid(column=0, row=6)
buttonSelectAll = Button(frame_bot, width=10, text="전체선택", overrelief="solid", command=selectall, font=font)
buttonSelectAll.grid(column=0, row=7)
buttonDeSelectAll = Button(frame_bot, width=10, text="전체취소", overrelief="solid", command=deselectall, font=font)
buttonDeSelectAll.grid(column=0, row=8)

if __name__ == '__main__':
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:
        mainloop()
    
    # mainloop()