ipHost = ''
command = '' 
processDone = False
status_connection = 0  #0 : disconnect, 1 : connecting, 2 : connected
src_screen = None

def init():
    global ipHost, command, status_connection
    ipHost = ''
    command = '' 
    status_connection = 0
    src_screen = None
