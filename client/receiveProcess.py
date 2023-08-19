from GUI import communicate
import struct
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "GUI\\tempData\\processData.txt") 

def receiveProcess(clientsocket):
    numberProcess = struct.unpack('!I', clientsocket.recv(4))[0]
    print(numberProcess)
    processInfo = []
    for i in range(numberProcess):
        processInfo.append(clientsocket.recv(1024).decode())
    with open(file_path, 'w') as fo:
        for pcInfo in processInfo:
            fo.write(pcInfo + '\n')
    communicate.queue_to_main.put("displayprocess")

def receiveStatus(clientsocket):
    communicate.status = clientsocket.recv(1024).decode()
    communicate.queue_to_main.put(communicate.command + "_process")
