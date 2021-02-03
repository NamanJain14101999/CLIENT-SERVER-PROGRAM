import socket
import threading
list=[]
SUM="+"
SUB="-"
MUL="*"
DIV="/"
HEADER=64
PORT = 4456
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =(SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "dis"

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION]{addr} connected.")
    connected=True
    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            print(f"[{addr}] {msg}")

            if msg == DISCONNECT_MESSAGE:
                connected=False
                print("client dis connected")
                conn.close()
            elif msg == SUM:
                sum=list[0]+list[1]
                sum=str(sum)
                conn.send(sum.encode(FORMAT))
                list.clear()
            elif msg == SUB:
                diff=list[0]-list[1]
                diff=str(diff)
                conn.send(diff.encode(FORMAT))
                list.clear()
            elif msg == MUL:
                diff=list[0]*list[1]
                diff=str(diff)
                conn.send(diff.encode(FORMAT))
                list.clear()
            elif msg == DIV:
                diff=list[0]/list[1]
                diff=str(diff)
                conn.send(diff.encode(FORMAT))
                list.clear()
            elif msg=="client":
                conn.send("client-server conntected".encode(FORMAT))
            else:
                list.append(int(msg))


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn , addr =server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()

print("[STARTING] server is starting ")
start()
