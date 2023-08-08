import struct

    
def receiveProcess(clientsocket):
    numberProcess = struct.unpack('!I', clientsocket.recv(4))[0]
    print(numberProcess)
    processInfo = [];
    for i in range(numberProcess):
        processInfo.append(clientsocket.recv(1024).decode())
        print(processInfo[-1])

def receiveStatus(clientsocket):
    print(clientsocket.recv(1024).decode())