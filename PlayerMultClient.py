import socket
import logging
from sys import stdout

from playermulttypes.SendType import SendType
from network.Connection import Connection
from packet.NameTransferPacket import NameTransferPacket


class PlayerMultClient:
    def __init__(self, hostIP: str, hostPort: int):
        self.hostIP = hostIP
        self.hostPort = hostPort
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.hostIP, self.hostPort))

    def tick(self):
        a = NameTransferPacket("User123").serilize()
        print(a)
        self.socket.send(a)

    def disconnect(self):
        self.socket.close()