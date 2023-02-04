from packet.Packet import Packet
from utils.Packer import Packer

class HandshakeAcceptedPaket(Packet):
    def __init__(self, authKey):
        super(HandshakeAcceptedPaket, self).__init__(2, {
            "AuthKey": authKey
        })

    def serilize(self) -> bytes:
        buffer = bytes()
        buffer = Packer.writeUnsingedShort(buffer, self.id)
        buffer = Packer.writeInt(buffer, self.data.get("AuthKey"))
        return buffer