from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))

print("The server is ready to receive")

while True:
    sentence, clientAddress = serverSocket.recvfrom(2048)
    try:
        with open(sentence.decode(), "r") as file:
            l = file.read(2048)
            serverSocket.sendto(l.encode(), clientAddress)
            print(f"Sent back to client: {l}")
    except FileNotFoundError:
        serverSocket.sendto("File not found.".encode(), clientAddress)
