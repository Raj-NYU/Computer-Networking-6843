# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(1)
    #print('Listening...')
    # fill in end

    while True:
        # Establish the connection
        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() 
        try:

            try:
                message = connectionSocket.recv(2048).decode()  
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()  

                # Send one HTTP header line into socket.
                connectionSocket.send("HTTP/1.0 200 OK\r\r".encode())
                connectionSocket.send("Content-Type: text/html\r\n".encode())
                connectionSocket.send(message.encode())
                

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                # Send response message for file not found (404)
                #print('404 Not Found')
                connectionSocket.send('HTTP/1.0 404 NOT FOUND\r\n'.encode())
                connectionSocket.close()
                # Close client socket
                

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
