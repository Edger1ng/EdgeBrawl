from ByteStream.Writer import Writer
from Utils.Helpers import Helpers
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

class LogicBP(Writer):
    def __init__(self, client, player, c, i, b, s, p):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.c = c
        self.i = i
        self.b = b
        self.p = p
        self.s = s

    def encode(self):
        self.writeVInt(203) # Command
        
        self.writeVInt(0)
        self.writeVInt(1) # Multipler
        self.writeVInt(100) # type (box id)
        self.writeVInt(1) # Reward Count
        
        self.writeVInt(self.c)
        self.writeDataReference(16, self.b)
        self.writeVInt(self.i)
        self.writeDataReference(self.s[0], self.s[1])# 29
        self.writeDataReference(self.p, self.p)# 52
        self.writeDataReference(0, 0)# 23
        self.writeVInt(0)
        
        self.writeBool(True) # ForcedDrops

        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeLogicLong(0)
        