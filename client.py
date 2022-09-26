import socket, threading


#Define contants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

def send_message():
    '''Send a message to the server to be broadcasted'''
    while True:
        message = input("")
        client_socket.send(message.encode(ENCODER))

def receive_message():
    '''Receive an incoming messsage from the server'''
    while True:
        try:
            #receive an incoming message from server
            message = client_socket.recv(BYTESIZE).decode(ENCODER)

            #Check for the name flag, else show the message
            if message == "NAME":
                name = input("What is your name: ")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            #An error occured, close the connection
            print("An error occured...")
            client_socket.close()
            break


#Create threads to continuously send and receive messages
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)

#Start the client
receive_thread.start()
send_thread.start()