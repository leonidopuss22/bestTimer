from tkinter import ttk
from tkinter import *
import tkinter
import tkinter.messagebox
from ttkthemes import themed_tk as tk
from notification import *

notificationtext = "Not defined"
selectedtime = 1
root = tk.ThemedTk()
root.geometry('350x440+200+100')
root.resizable(False, False)
root.get_themes()
root.set_theme("breeze")

statusbar = ttk.Label(root, text="Добро пожаловать в BestTimer", relief=SUNKEN, anchor=W, font='Calibri 11 italic')
statusbar.pack(side=BOTTOM, fill=X)

menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)

root.title("BestTimer")
root.iconbitmap('icons/logo.ico')

mainframe = Frame(root)
mainframe.pack(side=BOTTOM, padx=50, pady=20, fill=X)
fieldframe = Frame(root)
fieldframe.pack(side=TOP)
timeframe = Frame(root)
timeframe.pack(side=BOTTOM, padx=30, pady=10)

timelabel = ttk.Label(timeframe, text="Через").pack()
entryNumber = ttk.Entry(timeframe)
entryNumber.pack(side=LEFT)

list=ttk.Combobox(timeframe, width=50, height=20, textvariable=selectedtime, state="readonly")
list['values'] = ["секунд", "минут", "часов"]
list.current(1)
list.pack(side=LEFT)

label = ttk.Label(mainframe, text="Укажите текст напоминания").pack()
entryText = ttk.Entry(mainframe, textvariable=notificationtext)
entryText.pack(fill=X)
global signed
signed = False
def count(text):
    global signed
    global time
    if list.get() == "минут":
        time = int(entryNumber.get()) * 60
    elif list.get() == "часов":
        time = int(entryNumber.get()) * 3600
    elif list.get() == "секунд":
        time = int(entryNumber.get())

    alert = ttk.Label(fieldframe, text=f"Установлено напоминание", font='17')
    alert2 = ttk.Label(fieldframe, text=f"{text}", font='13')
    if not signed:
        alert.pack(side=TOP, pady=10)
        alert2.pack(side=BOTTOM)
        signed = True
    alert.after(time * 1000, lambda:alert.pack_forget())
    alert2.after(time * 1000, lambda:alert2.pack_forget())
    start_thread(text, time)

setbtn = ttk.Button(mainframe, text="Установить", command=lambda:count(entryText.get()))
setbtn.pack()

def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
