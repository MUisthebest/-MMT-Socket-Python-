import struct

def receiveRunningApp(clientsocket):
    numberRunningApp = struct.unpack('!I', clientsocket.recv(4))[0]
    print(numberRunningApp)
    runningAppInfo = [];
    for i in range(numberRunningApp):
        runningAppInfo.append(clientsocket.recv(1024).decode())
        print(runningAppInfo[-1])

    

