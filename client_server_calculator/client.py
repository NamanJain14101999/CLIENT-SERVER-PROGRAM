import socket
HEADER = 64
PORT =4456
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

def result():
    print("message recevied from server ")
    sum=client.recv(HEADER).decode(FORMAT)
    print(sum)

    while True:
        print(" eneter first number ")
        a=input()
        send(a)
        print(" eneter second number ")
        b=input()
        send(b)
        print("enter + for add")
        print("enter - for sub")
        print("enter * for mul")
        print("enter / for div")
        print("enter dis for disconnect")
        request=input()
        if request=="dis":
            send(request)
            client.close()
            exit("client disconnected")
        else:
            send(request)
            result()


send("client")
result()
