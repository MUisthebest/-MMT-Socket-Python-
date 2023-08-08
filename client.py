import socket
from PIL import Image
import receiveScreenShot
import receiveRunningApp
import receiveProcess


def start_client():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = '192.168.2.100'
    host = 'localhost'
    port = 9999
    clientsocket.connect((host, port))
    while True:
        command = input("Enter message to send to server: ")
        clientsocket.send(command.encode('ascii'))
        command = list(map(str, command.split()))
        flag = command[0]
        parameter = -1
        if len(command) > 1 : parameter = command[1]
        
        if flag == "screenshot": receiveScreenShot.readImage(clientsocket)
        elif flag == "listprocess": receiveProcess.receiveProcess(clientsocket)
        elif flag == "killprocess": receiveProcess.receiveStatus(clientsocket)
        elif flag == "listrunningapp": receiveRunningApp.receiveRunningApp(clientsocket)
        elif flag == "shutdown": break
        else:
            data = clientsocket.recv(1024)
            print('Received from server: ', data.decode('ascii'))
        if flag == 'QUIT':
            break
    clientsocket.close()

if __name__ == "__main__":
    start_client()
