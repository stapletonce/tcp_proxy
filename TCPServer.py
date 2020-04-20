import socket
import threading

bind_ip = "172.17.1.5"
bind_port = 21

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))

# this is our client handling thread
def handle_client(client_socket):

    # print out what the client sends
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    # send back a packet
    message = "ACK!"
    client_socket.send(message.encode())

    client_socket.close()

while True:

    client,addr = server.accept()

    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # spin up our client thred to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
