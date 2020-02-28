# -*- coding: utf-8 -*-

from socket import socket

def open_connect_to_client():
    skc = socket()
    skc.bind(("127.0.0.1", 8000))
    skc.listen(1)
    connection, address = skc.accept()
    print(f"[*] new connection from {address}")

    while True:
        cmd = input("user:~> ")
        if "terminate" in cmd:
            print("[*] close conection :(")
            connection.send('terminate'.encode())
            connection.close()
            break
        elif cmd == "":
            print("[*] empty string !!!")
            pass
        else:
            connection.send(cmd.encode())
            print(connection.recv(1024).decode())


if __name__ == "__main__":
    open_connect_to_client()
