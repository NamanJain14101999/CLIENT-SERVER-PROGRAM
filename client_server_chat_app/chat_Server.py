import socket
import threading

HEADER=64
PORT = 1244
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
                print("client closed")
                conn.close()
            else:
                print("server write")
                s=input()
                conn.send(s.encode(FORMAT))


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn , addr =server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print()

print("[STARTING] server is starting ")
start()
