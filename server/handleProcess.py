import psutil
import struct
import signal
import errno
import os

def killProcess(clientsocket, pid):
    try:
        os.kill(pid, signal.SIGTERM)
        clientsocket.send("kill_ok".encode())
    except:
        clientsocket.send("kill_err".encode())

# Iterate over all running process
def listProcess(clientsocket):
    
    all_pids = psutil.pids()
 
    numberProcess = len(all_pids)

    clientsocket.sendall(struct.pack('!I', numberProcess))

    for proc in psutil.process_iter():
        try:
            # Get process details as a dictionary
            process = proc.as_dict(attrs=['pid', 'name', 'num_threads'])
            processInfo = f'{process["pid"]},{process["name"]},{process["num_threads"]}'
            clientsocket.send(processInfo.encode())  
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass




# if __name__ == '__main__':
#     listProcess(clie)