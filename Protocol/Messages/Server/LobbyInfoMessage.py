from ByteStream.Writer import Writer
import psutil
from datetime import datetime, date, time

class LobbyInfoMessage(Writer):

    def __init__(self, client, player, count):
        super().__init__(client)
        self.id = 23457
        self.player = player
        self.count = count

    def encode(self):
        ram_usage = int(psutil.virtual_memory().used / (1024 * 1024))
        cpu_usage = int(psutil.cpu_percent())
        a = str(datetime.utcnow())
        self.writeVInt(self.count)
        self.writeString(f'--------\n@edgebrawl\nRAM Usage: {ram_usage} MB\nCPU Usage: {cpu_usage} %\n--------')


        self.writeVInt(0) # array
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
