import win10toast
from threading import Thread
import threading
import time
event = threading.Event()

def start_notification(text, totaltime:int):
    time.sleep(totaltime)
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(
        "Напоминание",
        text,
        icon_path="icons/logo.ico",
        threaded=True
    )
    change_signed(False)

def change_signed(new_signed):
    import main
    main.signed = new_signed

def start_thread(text, totaltime):
    threading._start_new_thread(start_notification, (text, totaltime))
