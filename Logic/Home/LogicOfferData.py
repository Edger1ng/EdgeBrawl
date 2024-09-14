import json
from datetime import datetime
import time


class LogicOfferData:
    shop_resources = json.loads(open('shop.json', 'r', encoding="utf-8").read())

    gold_packs = shop_resources['GoldPacks']
    gold_cost, gold_amount = [], []

    for x in gold_packs:
        gold_cost.append(x['Cost'])
        gold_amount.append(x['Amount'])

    boxes = shop_resources['Boxes']
    token_doubler = shop_resources['TokenDoubler']

    offers = shop_resources['Offers']


    def encodeShopOffers(self):
        self.writeVInt(len(LogicOfferData.offers))  # Offers Array
        for x in LogicOfferData.offers:
            num_offers = 1  # По умолчанию только одна акция
            if (x['OfferID2'] != 0):
                num_offers = 2
            if (x['OfferID3'] != 0):
                num_offers = 3

            self.writeVInt(num_offers)
            print("Start encodeng")

            self.writeVInt(x['OfferID'])
            self.writeVInt(x['Multiplier'])
            self.writeDataReference(x['DataReference'][0], x['DataReference'][1])  # Offer DataReference
            self.writeVInt(x['SkinID'])
            print("Encoded 1")

            if num_offers > 1:
                self.writeVInt(x['OfferID2'])
                self.writeVInt(x['Multiplier2'])
                self.writeDataReference(x['DataReference2'][0], x['DataReference2'][1])
                self.writeVInt(x['SkinID2'])
                print("Encoded 2")

            if num_offers > 2:
                self.writeVInt(x['OfferID3'])
                self.writeVInt(x['Multiplier3'])
                self.writeDataReference(x['DataReference3'][0], x['DataReference3'][1])
                self.writeVInt(x['SkinID3'])
                print("Encoded 3")

            self.writeVInt(x['ShopType'])

            self.writeVInt(x['Cost'])
            timer_timestamp = self.convert_time_str_to_timestamp(x['Timer'])
            self.writeVInt(timer_timestamp - int(time.time()))
            print("Encoded Offers Half 2")

            self.writeVInt(1)
            self.writeVInt(100)
            # self.writeUInt8(1)
            seid = False
            forced = False
            if x['ID'] in self.player.buyed:
                seid = True
                forced = True
                print("Buyed")
            if x['BrawlerID'] or x['BrawlerID2'] or x['BrawlerID3'] not in self.player.brawlers_unlocked:
                seid = True
                print("Brawler ID")
            # elif (x['SkinID'] or x['SkinID2'] or x['SkinID3'] in self.player.unlocked_skins):
            # self.writeBoolean(True)
            # print("SkinID")
            if timer_timestamp - int(time.time()) <= 0:
                seid = True
                forced = True
                print("Timer ended")
            if self.player.trophies >= x['RequiredTrophies']:
                seid = False
                print("Trophies")
            if self.player.trophies >= x['MaxTrophies']:
                seid = True
                print("Max Trophies")
            start_time_timestamp = self.convert_time_str_to_timestamp(x['StartTime'])
            if start_time_timestamp - int(time.time()) != 0:
                if start_time_timestamp - int(time.time()) <= 0:
                    seid = False
                else:
                    forced = True
            if int(x['SkinID'] or x['SkinID2'] or x['SkinID3']) in self.player.unlocked_skins:
                if int(x['SkinID'] or x['SkinID2'] or x['SkinID3']) != 0:
                    broooo = 0
                    while broooo == 100:
                        print("WOW")
                        broooo = broooo + 1
                    forced = True
                else:
                    seid = False
            if int(x['BrawlerID'] or x['BrawlerID2'] or x['BrawlerID3']) in self.player.brawlers_unlocked:
                if int(x['BrawlerID'] or x['BrawlerID2'] or x['BrawlerID3']) != 0:
                    broooo2 = 0
                    while broooo2 == 100:
                        print("WOW2")
                        broooo2 = broooo2 + 1
                    forced = True
                else:
                    seid = False
            else:
                if (x['Required'] != 0):
                    if (x['Required'] in self.player.buyed):
                        seid = False
                        print("Required None")
                    if (x['Required'] not in self.player.buyed):
                        seid = True
                        print("Required")
                if (x['PremiumOffer'] == True):
                    if self.player.premium == False:
                        seid = True
                    else:
                        seid = False
            if forced:
                self.writeBoolean(True)
            else:
                self.writeBoolean(seid)
            print("Encoded Offers Half 3")

            self.writeUInt8(0)
            self.writeVInt(x['ShopDisplay'])
            self.writeVInt(x['OldCost'])
            self.writeVInt(0)

            self.writeInt(0)
            self.writeStringReference(x['OfferText'])

            self.writeUInt8(0)
            self.writeString(x['BGR'])
            self.writeVInt(0)
            self.writeUInt8(0)
            self.writeVInt(2)
            self.writeVInt(0)

    def convert_time_str_to_timestamp(self, time_str):
        try:
            dt = datetime.strptime(time_str, "%d-%m-%Y %H:%M")
            return int(time.mktime(dt.timetuple()))
        except ValueError:
            print(f"Invalid time format: {time_str}")
            return 0