from ByteStream.Writer import Writer
from Utils.Helpers import Helpers
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
import random

class PinPack(Writer):
    def __init__(self, client, player, id):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.id = id

    def encode(self):
            self.player.delivery_items = {
                'Count': 1,
                'Type': 0,
                'Items': []
            }
            pin = {'Amount': 1, 'DataRef': [0, 0], 'DataSkin': [0, 0], 'DataPin':[52, self.id], 'Value': 11 }
            self.player.delivery_items['Items'].append(pin)
            self.player.delivery_items['Type'] = 100
            AvailableServerCommandMessage(self.client, self.player, 203).send()
        