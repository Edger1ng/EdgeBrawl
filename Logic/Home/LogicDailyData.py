from datetime import datetime
from Logic.Home.LogicShopData import LogicShopData
from Logic.Home.LogicOfferData import LogicOfferData
import json, time

class LogicDailyData:

    def encode(self):
        config_file = json.loads(open('config.json', 'r', encoding="utf-8").read())
        time_stamp = int(datetime.timestamp(datetime.now()))

        self.writeVInt(time_stamp)
        self.writeVInt(time_stamp)

        self.writeVInt(self.player.trophies)
        self.writeVInt(self.player.high_trophies)
        self.writeVInt(self.player.high_trophies)

        self.writeVInt(self.player.trophy_reward)
        self.writeVInt(self.player.exp_points)

        self.writeDataReference(28, self.player.profile_icon)
        self.writeDataReference(43, self.player.name_color)

        self.writeVInt(50)
        for x in range(50):
            self.writeVInt(x)

        self.writeVInt(len(self.player.selected_skins))
        for x in self.player.selected_skins:
            self.writeDataReference(29, self.player.selected_skins[x])

        self.writeVInt(len(self.player.unlocked_skins))
        for x in self.player.unlocked_skins:
            self.writeDataReference(29, x)

        self.writeVInt(0)  # Unknown Array
        for x in range(0):
            self.writeDataReference(0,0)

        self.writeVInt(0)      # Leaderboard Global TID
        self.writeVInt(self.player.trophies)  # Trophy Road Reached Icon
        self.writeVInt(0)      # Unknown
        self.writeVInt(0)      # Unknown

        self.writeUInt8(0)     # Is Token Limit Reached

        self.writeVInt(self.player.token_doubler)
        self.writeVInt(int(config_file['TrophyTimer']) - int(time.time()))  # Trophy Road Timer
        self.writeVInt(0)      # Power Play Timer
        self.writeVInt(int(config_file['PassTimer']) - int(time.time()))  # Brawl Pass Timer

        self.writeVInt(0)  # Unknown

        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeUInt8(4) # Shop Token Doubler

        self.writeVInt(2) # Unknown
        self.writeVInt(2) # Unknown
        self.writeVInt(2) # Unknown

        self.writeVInt(0) # Name Change Cost
        self.writeVInt(0) # Name Change Timer


        LogicOfferData.encodeShopOffers(self)

        self.writeVInt(0)  # AdStatus
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeVInt(200) # Available Battle Tokens
        self.writeVInt(0)   # Time till Bonus Tokens

        self.writeVInt(0)  # Unknown Array
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(1)
        self.writeVInt(1)  # Unknown

        self.writeDataReference(16, self.player.home_brawler)

        self.writeString(self.player.region)
        self.writeString(self.player.content_creator)

        self.writeVInt(1)  # Unknown Array
        for x in range(1):
            self.writeInt(3)
            self.writeInt(self.player.pass_tokens)

        self.writeVInt(0)  # CooldownEntry
        for x in range(0):
            self.writeVInt(0)
            self.writeDataReference(0, 0)
            self.writeVInt(0)

        self.writeVInt(1)  # BrawlPassSeasonData
        for x in range(1):
            self.writeVInt(1)  # Current Season
            self.writeVInt(self.player.pass_tokens)  # Pass Tokens
            self.writeBool(self.player.bp_activated)
            self.writeVInt(-1)  # Pass Progress

            bitList = [0, 0, 0, 0]

            for i in self.player.bpdonate_claimed:
                if i < 30:
                    bitList[0] += (2 ** (i+2))
                elif i > 29 and i < 62:
                    bitList[1] += (2 ** ((i-32)+2))
                elif i > 61 and i < 80:
                    bitList[2] += (2 ** ((i-64)+2))
            
            print(bitList)

            self.writeInt8(1)
            for i in bitList:
                self.writeInt(i)

            bitList = [0, 0, 0, 0]


            for i in self.player.bpfree_claimed:
                if i < 30:
                    bitList[0] += (2 ** (i+2))
                elif i > 29 and i < 62:
                    bitList[1] += (2 ** ((i-32)+2))
                elif i > 61 and i < 80:
                    bitList[2] += (2 ** ((i-64)+2))

            self.writeInt8(1)
            for i in bitList:
                self.writeInt(i)

        self.writeVInt(0)  # ProLeagueSeasonData
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeBoolean(True) # LogicQuests
        if True:
            self.writeVInt(0)
            for x in range(0):
                self.writeVInt(0)     # Unknown
                self.writeVInt(0)     # Unknown
                self.writeVInt(1)     # Mission Type
                self.writeVInt(2)     # Achieved Goal
                self.writeVInt(8)     # Quest Goal
                self.writeVInt(10)    # Tokens Reward
                self.writeVInt(0)     # Unknown
                self.writeVInt(0)     # Current level
                self.writeVInt(0)     # Max level
                self.writeVInt(1)     # Quest Type
                self.writeUInt8(2)    # Quest State
                self.writeDataReference(16, 0)
                self.writeVInt(0)     # GameMode
                self.writeVInt(0)     # Unknown
                self.writeVInt(0)     # Unknown

        # Emotes Array
        self.writeBoolean(True)
        if True:
            self.writeVInt(len(self.player.emotes_id))
            for x in self.player.emotes_id:
                self.writeDataReference(52, x)
                self.writeVInt(1)     # Unknown
                self.writeVInt(1)     # Unknown
                self.writeVInt(1)     # Unknown
