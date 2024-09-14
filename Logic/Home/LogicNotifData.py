from datetime import datetime


class Notifications:

    def EncodeNotification(self):
        notif_data = self.player.notifications
        count = len(notif_data)
        self.writeVInt(count)
        for i in range(count):
            item = notif_data[str(i)]

            self.writeVInt(item['NotifID'])
            self.writeInt(i)
            if item['NotifRead'] == "false":
                self.writeBoolean(False)
            else:
                self.writeBoolean(True)

            self.writeInt(int(datetime.timestamp(datetime.now())-item['NotifTime']))
            self.writeString(item['Notiftext'])

            if item['NotifID'] == 81:
                self.writeVInt(0)