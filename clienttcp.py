from socket import *

serverName = "127.0.0.1"
serverPort = 12000

# Create a client socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))  # Connect to the server

# Get input from the user (filename)
filename = input("Enter the filename: ")
clientSocket.send(filename.encode())  # Send the filename to the server

# Receive the response from the server
response = clientSocket.recv(1024).decode()
print("From Server:", response)

clientSocket.close()  # Close the connection
