# -*- coding: utf-8 -*-

import socket

def open_connect_to_client():
    skc = socket.socket()
    skc.bind(("192.168.1.4", 8000))
    skc.listen(1)
    connection. address = skc.accept()
    print(f"[*] new connection from {address}")

    while True:
        cmd = input("user:~>")
        if "terminate" in cmd:
            print("[*] close conection :(")
            connection.send('terminate'.encode())
            connection.close()
            break
        else:
            connection.send(cmd.encode())
            print(connection.recv(1024).decode())

if __name__ == "__main__":
    open_connect_to_client()