import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",1234))
s.listen(10)
client, client_address = s.accept()
print("Client has connected with address: {}".format(client_address))

msg = client.recv(1024)

# repeat as long as message
# string are not empty

while msg:
    print('Recived:' + msg.decode())
    msg = client.recv(1024)
s.close()
