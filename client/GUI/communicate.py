import queue

ipHost = ''
command = '' 
processDone = False
status_connection = 0  #0 : disconnect, 1 : connecting, 2 : connected
src_screen = None
blackListCommand = ["saveimage"]
queue_to_main = None
keylogger_txt = None
frameRunningApp = None 
frameProcess = None
status = ""

def init():
    global ipHost, command, status_connection, src_screen, queue_to_main, keylogger_txt
    global frameRunningApp, frameProcess, status
    ipHost = ''
    command = '' 
    status_connection = 0
    src_screen = None
    queue_to_main = None
    keylogger_txt = None
    frameRunningApp = None 
    frameProcess = None
    status = None

