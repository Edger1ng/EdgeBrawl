from ByteStream.Writer import Writer
from Logic.Home.LogicBoxData import LogicBoxData

class LogicGiveDeliveryItemsCommand(Writer):

    def encode(self):

        self.writeVInt(0)
        self.writeVInt(self.player.delivery_items['Count']) # multiplier

        for y in range(self.player.delivery_items['Count']):
            # DeliveryUnit
            type = self.player.delivery_items['Type']
            self.writeVInt(type)
            if type != 100:
                rewards = LogicBoxData.randomize(self, type)['Rewards']
            else:
                rewards = self.player.delivery_items['Items']

            self.writeVInt(len(rewards))

            for x in rewards:
                # GatchaDrop
                self.writeVInt(x['Amount'])
                self.writeDataReference(x['DataRef'][0], x['DataRef'][1]) if x['DataRef'][0] == 16 else self.writeVInt(0)
                self.writeVInt(x['Value'])
                self.writeDataReference(x['DataRef'][0], x['DataRef'][1]) if x['DataRef'][0] == 29 else self.writeVInt(0)
                self.writeDataReference(x['DataRef'][0], x['DataRef'][1]) if x['DataRef'][0] == 52 else self.writeVInt(0)
                self.writeDataReference(x['DataRef'][0], x['DataRef'][1]) if x['DataRef'][0] == 23 else self.writeVInt(0)
                self.writeVInt(0)

        self.writeVInt(0)
        if self.player.delivery_type == 0:
            self.writeVInt(0)
            self.writeVInt(0)
        else:
            if self.player.delivery_type == 10:
                self.writeVInt(6)
                self.writeVInt(self.player.trophies + 1)
            elif self.player.delivery_type == 100:
                self.writeVInt(10)
                self.writeVInt(self.player.bp_progress + 2)
            elif self.player.delivery_type == 101:
                self.writeVInt(9)
                self.writeVInt(self.player.bp_progress + 2)
            else:
                self.writeVInt(0)
            if self.player.delivery_type == 1:
                self.writeVInt(0)
            else:
                self.writeVInt(1)

        self.player.delivery_type = 0
        self.player.bp_progress = 0
 # ForcedDrops

