import socket
i=0
HEADER = 64
PORT =1244
FORMAT ='utf-8'
DISCONNECT_MESSAGE = "dis"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length+=b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

while True:
    if i==0:
        print("ennter dis for disconnection")
        i=i+1
    s=input("client-> \n")
    if s=="dis":
        send(s)
        break
    else:
        send(s)
        print("server  ->>")
    print(client.recv(HEADER).decode(FORMAT))
client.close()

