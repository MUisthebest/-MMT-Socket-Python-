import psutil
import struct
from pywinauto import Desktop

def listRunningApp(clientsocket):

    windows = Desktop(backend="uia").windows()
    numberRunningApp = len(windows)
    if windows[0].window_text() == "Taskbar" : numberRunningApp -= 1
    clientsocket.sendall(struct.pack('!I', numberRunningApp))
    
    for w in windows:
        full_title = w.window_text()
        if full_title == "Taskbar": continue
        if ' - ' in full_title:
            app_name = full_title.rsplit(' - ', 1)[1]
        else:
            app_name = full_title
        proc_id = w.process_id()

        try:
            process = psutil.Process(proc_id)
            thread_count = process.num_threads()
        except psutil.NoSuchProcess:
            continue
        appInfo = f'{app_name} {proc_id} {thread_count}'
        clientsocket.send(appInfo.encode())
