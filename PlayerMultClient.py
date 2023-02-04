import socket
import logging

from sys import stdout

from playermulttypes.SendType import SendType
from network.Connection import Connection
from utils.Queue import Queue

from packet.Packet import Packet
from packet.HandshakeRequestPacket import HandshakeRequestPaket
from packet.HandshakeAcceptedPacket import HandshakeAcceptedPaket

BUFFER_SIZE = 2048
PROTOCOL_VERSION = 1

class PlayerMultClient:
    def __init__(self, hostIP: str, hostPort: int):
        self.hostIP = hostIP
        self.hostPort = hostPort
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dataQueue = Queue()

        self.connected = False
        self.awaitHandshakeAccept = False

    def connect(self):
        res = self.socket.connect_ex((self.hostIP, self.hostPort))

        if res == 0:
            self.addData(HandshakeRequestPaket(PROTOCOL_VERSION))
            self.awaitHandshakeAccept = True

    def recieveData(self):
        data = self.socket.recv(BUFFER_SIZE)

        if data:
            packed_id = data[:2]
            print(Packet.getPacketByID(packed_id))

    def addData(self, packet: Packet):
        self.dataQueue.push(packet.serilize())

    def sendData(self):
        data = self.dataQueue.pop()
        if data: self.socket.send(data)

    def tick(self):
        self.sendData()
        self.recieveData()

    def disconnect(self):
        self.socket.close()