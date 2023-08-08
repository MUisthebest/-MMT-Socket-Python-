import socket
import threading
import handleProcess 
from sendScreenShot import sendScreenShot


def handleClientSocket(clientsocket):
    while True:
        try:
            data = clientsocket.recv(1024).decode('ascii')
            if not data: 
                print("goodbye")
                break
            print("Received from client: ", data)
            if data == "screenshot": sendScreenShot(clientsocket)
            elif data == "listprocess": handleProcess.listProcess(clientsocket) 
            else:
                msg = 'Echo => '+ data
                clientsocket.send(msg.encode('ascii'))
        except: clientsocket.close()
    clientsocket.close()

def start_server():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 9999
    serversocket.bind((host, port))
    serversocket.listen(5)
    while True:
        print("Waiting for client...")
        clientsocket, addr = serversocket.accept()
        print("Got a connection from %s" % str(addr))
        client_handler = threading.Thread(target=handleClientSocket, args=(clientsocket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
