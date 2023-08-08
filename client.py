import socket
from PIL import Image
import receiveScreenShot



def start_client():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = '192.168.2.100'
    host = 'localhost'
    port = 9999
    clientsocket.connect((host, port))
    while True:
        message = input("Enter message to send to server: ")
        clientsocket.send(message.encode('ascii'))
        if message == "screenshot": receiveScreenShot.readImage(clientsocket)
        else:
            data = clientsocket.recv(1024)
            print('Received from server: ', data.decode('ascii'))
        if message == 'QUIT':
            break
    clientsocket.close()

if __name__ == "__main__":
    start_client()
