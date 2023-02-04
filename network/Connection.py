from socket import socket

class Connection:
    def __init__(self, s: socket, address: str, identifier: any):
        self.socket = s
        self.address = address
        self.identifier = identifier

    def __repr__(self):
        return f"Connection from {self.address[0]} ({self.identifier})"