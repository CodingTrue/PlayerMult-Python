from packet.Packet import Packet
from utils.Packer import Packer

class HandshakeRequestPaket(Packet):
    def __init__(self, protocolVersion):
        super(HandshakeRequestPaket, self).__init__(0, {
            "ProtocolVersion": protocolVersion
        })

    def serilize(self) -> bytes:
        buffer = bytes()
        buffer = Packer.writeUnsingedShort(buffer, self.id)
        buffer = Packer.writeUnsingedShort(buffer, self.data.get("ProtocolVersion"))
        return buffer