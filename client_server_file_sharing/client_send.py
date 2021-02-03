import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
HEADER = 1024

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    file = open("server_data/server_data.txt", "r")
    data = file.read()
    client.send("server_data.txt".encode(FORMAT))
    msg = client.recv(HEADER).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    client.send(data.encode(FORMAT))
    msg = client.recv(HEADER).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    file.close()
    client.close()

main()
