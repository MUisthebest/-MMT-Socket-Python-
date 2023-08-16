import psutil
import struct
import signal
import os
import handleProcess
from pywinauto import Desktop

def killRunningApp(clientsocket, pid):
    try:
        os.kill(pid, signal.SIGTERM)
    except Exception as e:
        pass
    
    # Sending a response to the client about the result
    listRunningApp(clientsocket)

def checkValidApp(w):
    try:
        full_title = w.window_text()
        if full_title == "Taskbar" or full_title == "": return False
        proc_id = w.process_id()
        process = psutil.Process(proc_id)
        thread_count = process.num_threads()
    except psutil.NoSuchProcess:
        return False 
    if ' - ' in full_title:
        app_name = full_title.rsplit(' - ', 1)[1]
    else:
        app_name = full_title
    return f'{proc_id},{app_name},{thread_count}'


def send_string_list(client_socket, string_list):
    data = '|'.join(string_list).encode('utf-8')
    # Send the total byte length first
    client_socket.sendall(len(data).to_bytes(4, 'big'))
    # Send the data
    client_socket.sendall(data)


def listRunningApp(clientsocket):
    windows = Desktop(backend="uia").windows()
    runningApp = []
    for w in windows:
        tmp = checkValidApp(w)
        if (tmp == False) : continue 
        runningApp.append(tmp)
    send_string_list(clientsocket, runningApp)
    print("DONE")
