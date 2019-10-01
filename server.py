# -*- coding: utf-8 -*-

import socket

def open_connect_to_client():
    skc = socket.socket()
    skc.bind(("192.168.1.3", 8000))
    skc.listen(1)
    connection. address = skc.accept()
    print(f"[*] new connection from {address}")

    while True:
        cmd = input("user:~>")
        if "terminate" in cmd:
            print("[*] close conection :(")
            cmd.send('terminate'.encode())
            cmd.close()
            break
        else:
            cmd.send(cmd.encode())
            print(cmd.recv(1024).decode())

if __name__ == "__main__":
    open_connect_to_client()