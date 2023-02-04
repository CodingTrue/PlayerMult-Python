import socket
import logging

from time import sleep
from threading import Thread
from sys import stdout
from utils.Packer import Packer
from playermulttypes.SendType import SendType
from network.Connection import Connection

from packet.Packet import Packet
from packet.NameTransferPacket import NameTransferPacket

BUFFER_SIZE = 2048

class PlayerMultServer:
    instance = None

    def __init__(self, ip: str, port: int, maxConnectionCount: int = 10, sendType: SendType = SendType.safe):
        PlayerMultServer.instance = self

        logging.basicConfig(format="[%(asctime)s] (%(levelname)s) %(message)s", level=logging.DEBUG, handlers=[
            logging.StreamHandler(stdout),
            logging.FileHandler("log.log", mode="w")
        ])

        self.ip = ip
        self.port = port

        self.maxConnectionCount = maxConnectionCount

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))
        self.socket.settimeout(0.5)

        self.running = False

        self.connections = []
        self.dataProcessingThread = Thread(target=self.dataProcessing)

    def registerPackets(self):
        logging.info("Register Packets...")

        Packet.registerPacket(0, NameTransferPacket)

        logging.info("Registered Packets...")

    def addConnection(self, connection: Connection):
        self.connections.append(connection)

    def dataProcessing(self):
        while self.running:
            for connection in self.connections:
                data = connection.socket.recv(BUFFER_SIZE)
                if data:
                    packet_Id = Packer.readUnsingedShort(data[:2])
                    packet = Packet.getPacketByID(packet_Id)(data[2:].decode())
                    print(packet.data)
            sleep(0.05)

    def listen(self):
        try:
            s, address = self.socket.accept()

            logging.info(f"{address[0]} connected to Server")
            self.addConnection(Connection(s, address, "connection"))
        except socket.timeout: pass

    def tick(self):
        self.listen()

    def start(self):
        logging.info("Starting Server...")
        self.running = True
        self.registerPackets()
        self.dataProcessingThread.start()
        self.socket.listen(self.maxConnectionCount)
        logging.info("Listening for connections...")

    def close(self):
        logging.info("Closing Server...")
        self.running = False
        self.socket.close()