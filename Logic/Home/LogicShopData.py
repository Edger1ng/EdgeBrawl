import json
from datetime import datetime
import time

class LogicShopData:

    shop_resources = json.loads(open('shop.json', 'r', encoding="utf-8").read())

    gold_packs = shop_resources['GoldPacks']
    gold_cost, gold_amount = [], []

    for x in gold_packs:
        gold_cost.append(x['Cost'])
        gold_amount.append(x['Amount'])

    boxes = shop_resources['Boxes']
    token_doubler = shop_resources['TokenDoubler']

    offers = shop_resources['Offers']

    def encodeShopPacks(self):
        # Unknown
        self.writeArrayVint([20, 35, 75, 140, 290, 480, 800, 1250])
        self.writeArrayVint([1, 2, 3, 4, 5, 10, 15, 20])
        # Tickets
        self.writeArrayVint([10, 30, 80])
        self.writeArrayVint([6, 20, 60])
        # Gold
        self.writeArrayVint(LogicShopData.gold_cost)
        self.writeArrayVint(LogicShopData.gold_amount)
        print("Encoded Shop Packs")

    def encodeShopResources(self):
        time_stamp = int(datetime.timestamp(datetime.now()))

        self.writeVInt(time_stamp)
        LogicShopData.encodeBoxes(self)
        LogicShopData.encodeTokenDoubler(self)
        print("Encoded Shop Resources")

    def encodeBoxes(self):
        self.writeVInt(100) # Tokens for 1 Brawl Box
        self.writeVInt(10)  # Tokens for 1 Big Box

        self.writeVInt(LogicShopData.boxes[0]['Cost'])
        self.writeVInt(LogicShopData.boxes[0]['Multiplier'])

        self.writeVInt(LogicShopData.boxes[1]['Cost'])
        self.writeVInt(LogicShopData.boxes[1]['Multiplier'])


    def encodeTokenDoubler(self):
        self.writeVInt(LogicShopData.token_doubler[0]['Cost'])
        self.writeVInt(LogicShopData.token_doubler[0]['Amount'])
