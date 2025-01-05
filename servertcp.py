from socket import *

serverName = "127.0.0.1"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection established with {addr}")
    
    sentence = connectionSocket.recv(1024).decode()
    try:
        with open(sentence, "r") as file:
            l = file.read(1024)
            connectionSocket.send(l.encode())
    except FileNotFoundError:
        connectionSocket.send("File not found.".encode())
    
    connectionSocket.close()
