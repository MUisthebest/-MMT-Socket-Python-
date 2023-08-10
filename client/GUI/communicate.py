ipHost = ''
command = '' 
status_connection = 0  #0 : disconnect, 1 : connecting, 2 : connected

def init():
    global ipHost, command, status_connection
    ipHost = ''
    command = '' 
    status_connection = 0