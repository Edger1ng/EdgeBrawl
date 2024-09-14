from Logic.ClientHome import LogicClientHome
from Logic.ClientAvatar import LogicClientAvatar
from ByteStream.Writer import Writer
from datetime import datetime
import time

class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player
        self.time_stamp = int(datetime.timestamp(datetime.now()))

    def encode(self):

        LogicClientHome.encode(self)
        LogicClientAvatar.encode(self)

        self.writeVInt(self.time_stamp)

    def convert_time_str_to_timestamp(self, time_str):
        try:
            dt = datetime.strptime(time_str, "%d-%m-%Y %H:%M")
            return int(time.mktime(dt.timetuple()))
        except ValueError:
            print(f"Invalid time format: {time_str}")
            return 0