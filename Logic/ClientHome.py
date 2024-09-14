from Logic.Home.LogicDailyData import LogicDailyData
from Logic.Home.LogicConfData import LogicConfData
from Logic.Home.LogicNotifData  import Notifications

class LogicClientHome:

    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)

        self.writeLong(self.player.ID)

        Notifications.EncodeNotification(self)

        self.writeVInt(0)  # Unknown

        self.writeUInt8(0) # Unknown
