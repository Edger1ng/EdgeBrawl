from DataBase.DBManager import DB
import random
from ByteStream.Writer import Writer


class LogicBoxDataCommand(Writer):

    def __init__(self, client, player, boxid, mcbylkprtctrd={"V": False}):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.boxid = boxid
        self.brawler = 0
        self.randomBS = 0
        self.randomBS2 = 0
        self.reward = 0
        self.gold = 0
        self.gems = 0
        self.LkPrtctrd = mcbylkprtctrd

    def encode(self):
        self.reward = random.choice([2, 3, 4])  # ,3,4
        trophy = [8, 2, 7, 3, 9, 14, 22, 27, 30]
        unlocked_brawlers = [brawler for brawler, unlocked in self.player.UnlockedBrawlers.items() if
                             unlocked and int(brawler) < 39]
        if unlocked_brawlers:
            sampleK = 2 if len(unlocked_brawlers) >= 2 else len(unlocked_brawlers)
            random_bs = random.sample(unlocked_brawlers, k=sampleK)
            self.randomBS = random_bs[0]
            self.randomBS2 = random_bs[1]
        if self.reward == 2:
            if False:  # self.brawler in [37]:
                self.reward = 3
            else:
                for id, unlocked in self.player.UnlockedBrawlers.items():
                    if unlocked == 0 and int(id) not in trophy:
                        self.brawler = int(id)
                        break
                if self.brawler is not None:
                    if self.brawler == 0:
                        self.reward = 3
                    else:
                        self.brawler = self.brawler
                        self.player.UnlockedBrawlers[str(self.brawler)] = 1
                        DB.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.UnlockedBrawlers)
        if self.boxid == 6:
            self.boxid = 10
        elif self.boxid == 7:
            self.boxid = 12
        elif self.boxid == 8:
            self.boxid = 11
        elif self.boxid == 5:  # Brawl Box
            self.player.box = self.player.box - 100
            DB.update_player_account(self.player.token, 'box', self.player.box)
            self.boxid = 10
        elif self.boxid == 4:  # Big Box
            self.player.bigbox = self.player.box - 10
            DB.update_player_account(self.player.token, 'bigbox', self.player.bigbox)
            self.boxid = 12
        elif self.boxid == 3:  # Shop Box
            self.player.gems = self.player.gems - 80
            DB.update_player_account(self.player.token, 'gems', self.player.gems)
            self.boxid = 11

        if self.boxid == 1:  # Shop Big Box
            self.player.gems -= 30
            DB.update_player_account(self.player.token, 'gems', self.player.gems)
            self.boxid = 12
        elif self.boxid == 4:  # Shop Mega Box
            self.player.gems -= 80
            DB.update_player_account(self.player.token, 'gems', self.player.gems)
            self.boxid = 11

        if self.reward == 2:
            self.gold = random.randint(10, 200)
            self.gold += self.gold
            self.brawler = self.brawler
            DB.update_player_account(self.player.token, 'gold', self.player.gold)

        if self.reward == 3 or self.reward == 4:
            blat2 = random.randint(10, 100)
            blat1 = random.randint(10, 100)
            self.gold = random.randint(1, 178)
            self.player.brawlerPoints[str(self.randomBS2)] += blat2
            DB.update_player_account(self.player.token, 'brawlerPoints', self.player.brawlerPoints)
            self.player.brawlerPoints[str(self.randomBS)] += blat1
            DB.update_player_account(self.player.token, 'brawlerPoints', self.player.brawlerPoints)
            self.player.gold += self.gold
            DB.update_player_account(self.player.token, 'gold', self.player.gold)

        if self.reward == 4:
            blat2 = random.randint(10, 100)
            blat1 = random.randint(10, 100)
            self.gems = random.randint(1, 12)
            self.gold = random.randint(1, 178)
            self.player.brawlerPoints[str(self.randomBS2)] += blat2
            DB.update_player_account(self.player.token, 'brawlerPoints', self.player.brawlerPoints)
            self.player.brawlerPoints[str(self.randomBS)] += blat1
            DB.update_player_account(self.player.token, 'brawlerPoints', self.player.brawlerPoints)
            self.player.gold += self.gold
            self.brawler = self.brawler
            DB.update_player_account(self.player.token, 'gold', self.player.gold)
            self.player.gems += self.gems
            DB.update_player_account(self.player.token, 'gems', self.player.gems)

        # Box info
        self.writeVInt(203)  # CommandID
        self.writeVInt(0)  # Unknown
        self.writeVInt(1)  # Unknown
        self.writeVInt(self.boxid)  # BoxID
        # Box info end

        # Reward start
        self.writeVInt(self.reward)  # Reward count

        # Brawler start
        if self.reward == 1:
            # Brawler start
            self.writeVInt(1)  # Reward amount
            self.writeScId(16, int(self.brawler))  # CsvID 16
            self.writeVInt(1)  # Reward ID
            self.writeVInt(0)  # CsvID 29
            self.writeVInt(0)  # CsvID 52
            self.writeVInt(0)  # CsvID 23
            self.writeVInt(0)
            # Brawler end
            self.player.UnlockedBrawlers[str(self.brawler)] = 1
            DB.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.UnlockedBrawlers)
        if self.reward == 3:
            # gold start
            self.writeVInt(self.gold)  # Reward amount
            self.writeVInt(0)  # CsvID 16
            self.writeVInt(7)  # Reward ID
            self.writeVInt(0)  # CsvID 29
            self.writeVInt(0)  # CsvID 52
            self.writeVInt(0)  # CsvID 23
            self.writeVInt(0)  # ????
            # Upgrade points start
            self.writeVInt(blat1)  # Reward amount
            self.writeScId(16, int(self.randomBS))  # CsvID 16
            self.writeVInt(6)  # Reward ID
            self.writeVInt(0)  # CsvID 29
            self.writeVInt(0)  # CsvID 52
            self.writeVInt(0)  # CsvID 23
            self.writeVInt(0)
            # new
            self.writeVInt(blat2)  # Reward amount
            self.writeScId(16, int(self.randomBS2))  # CsvID 16
            self.writeVInt(6)  # Reward ID
            self.writeVInt(0)  # CsvID 29
            self.writeVInt(0)  # CsvID 52
            self.writeVInt(0)  # CsvID 23
            self.writeVInt(0)
            # Upgrade points end
            # Brawler start
        if self.reward == 4:
            # Gold Start
            self.writeVInt(self.gold)  # Reward amount
            self.writeVInt(0)  # CsvID 16
            self.writeVInt(7)  # Reward ID
            self.writeVInt(0)  # CsvID 29
            self.writeVInt(0)  # CsvID 52
            self.writeVInt(0)  # CsvID 23
            self.writeVInt(0)  # ????
            # Upgrade points start
            self.writeVInt(blat1)  # Reward amount
            self.writeScId(16, int(self.randomBS))  # CsvID 16
            self.writeVInt(6)  # Reward ID
            self.writeVInt(0)  # CsvID 29
            self.writeVInt(0)  # CsvID 52
            self.writeVInt(0)  # CsvID 23
            self.writeVInt(0)
            # new
            self.writeVInt(blat2)  # Reward amount
            self.writeScId(16, int(self.randomBS2))  # CsvID 16
            self.writeVInt(6)  # Reward ID
            self.writeVInt(0)  # CsvID 29
            self.writeVInt(0)  # CsvID 52
            self.writeVInt(0)  # CsvID 23
            self.writeVInt(0)
            # Upgrade points end
            # Brawler start

            self.writeVInt(self.gems)  # Reward amount
            self.writeVInt(0)  # CsvID 16
            self.writeVInt(8)  # Reward ID
            self.writeVInt(0)  # CsvID 29
            self.writeVInt(0)  # CsvID 52
            self.writeVInt(0)  # CsvID 23
            self.writeVInt(0)  # ????
            # Brawler start
        # Box end
        if not self.LkPrtctrd["V"]:
            for i in range(13):
                self.writeVInt(0)
        else:
            self.writeVInt(0)
            self.writeVInt(self.LkPrtctrd["R"])
            self.writeVInt(self.LkPrtctrd["L"])
            self.writeVInt(self.LkPrtctrd["S"])
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
