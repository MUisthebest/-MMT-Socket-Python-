import struct
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "GUI\\tempData\\apprunningData.txt") 

def receiveRunningApp(clientsocket):
    numberRunningApp = struct.unpack('!I', clientsocket.recv(4))[0]
    print(numberRunningApp)
    runningAppInfo = []
    for i in range(numberRunningApp):
        runningAppInfo.append(clientsocket.recv(1024).decode())
        # print(runningAppInfo[-1])
    with open(file_path, 'w', encoding="utf-8") as fo:
        for pcInfo in runningAppInfo:
            fo.write(pcInfo + '\n')
            # print(type(pcInfo))

    

