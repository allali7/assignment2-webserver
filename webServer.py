# import socket module
from socket import *
# In order to terminate the program
import sys

#define the web server function
def webServer(port=13331):
  #create a new server socket object
  #AF_inet is a adress family and means socket will use ipv4 addressing
  #Sock streams is a type of socket showing it will use tcp
  #so this is a tcp socket what will be used to listen on a specific ip address
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  #bind server socket to the port
  serverSocket.bind(("", port))

  #Fill in start
#listen for incomming connection on the server socket
  #the 1 says that it will listen to one client at a time, so if queue is full then it will reject connection
  serverSocket.listen(1)
  #Fill in end




#while true, loop forever to capture and incoming client connections
  while True:
    #Establish the connection

    #shows server is ready to accept connection
    print('Ready to serve...')

    #wait for the client to connect to the server and accept the connection
    #the accept method blocks the program from executinguntil a client
    #connects to the server socket. Then what is returned is an address to identify the client and
    #a client socket to send and receive data
    connectionSocket, addr =  serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      #recieve the client message
      #when the client connects to the server it send a message to the server which will be saved in "message" variable
      #so the server uses recv to recieve the message from the client socket
      #the message is max 1024 bytes
      message = connectionSocket.recv(1024) #Fill in start -a client is sending you a message   #Fill in end
      #extract the filename from the client message
      #split it into 2 words and take the word at index 1
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      #to read data in a html file which may contain images, it is best to read in binary form using rb
      # [1:] is a slice to remove the '/' usually as the first char in the file name
      #variable f can be used to read file content and send them to client
      f = open(filename[1:],"rb") #fill in start #fill in end)
      #fill in end

      #create an http header to send to the client
      #this creates byte string to that has the http response header that will be sent back to client
      #the content type will be text/html; charset utf8
      #b prefix means it is a byte string and not a regular string - this tell python to encode string in bytes
      # the \r\n represent new line sequence that is required in http protocol to seperate
      #headers from the body

      #Fill in start -This variable can store your headers you want to send for any valid or invalid request.
      #Content-Type above is an example on how to send a header as bytes

      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      #Fill in end

      #Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok? 
      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      #Fill in start
      connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
      #Send the http header to the client
      connectionSocket.send(outputdata)

      #Fill in end
               

      #Send the content of the requested file to the client
      for i in f: #for line in file
        #Fill in start - send your html file contents #Fill in end
        # no need to use encode bc we are using 'rb'
        connectionSocket.send(i)

      #close the file
      f.close()


      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      #Fill in start
      notFoundMessage = b"HTTP/1.1 404 Not Found\r\n\r\n"
      connectionSocket.send(notFoundMessage)

      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
