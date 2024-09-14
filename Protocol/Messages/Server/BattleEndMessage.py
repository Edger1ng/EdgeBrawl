from ByteStream.Writer import Writer
from DataBase.DBManager import DB

class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players, db: DB):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.type    = type
        self.result  = result
        self.players = players
        self.db = db

    def encode(self):

        brawler_trophies = self.player.brawlers_trophies[str(self.player.home_brawler)]
        old_tr = self.player.trophies

        self.writeVInt(self.type)
        self.writeVInt(self.result)
        if 0 <= brawler_trophies <= 49:
            win_val = 20
            lose_val = 0

        else:
            if 50 <= brawler_trophies <= 99:
                win_val = 8 * self.player.battle_multiplier
                lose_val = -1

            if 100 <= brawler_trophies <= 199:
                win_val = 8 * self.player.battle_multiplier
                lose_val = -2

            if 200 <= brawler_trophies <= 299:
                win_val = 8 * self.player.battle_multiplier
                lose_val = -3

            if 300 <= brawler_trophies <= 399:
                win_val = 8 * self.player.battle_multiplier
                lose_val = -4

            if 400 <= brawler_trophies <= 499:
                win_val = 8 * self.player.battle_multiplier
                lose_val = -5

            if 500 <= brawler_trophies <= 599:
                win_val = 8 * self.player.battle_multiplier
                lose_val = -6

            if 600 <= brawler_trophies <= 699:
                win_val = 8 * self.player.battle_multiplier
                lose_val = -7

            if 700 <= brawler_trophies <= 799:
                win_val = 8 * self.player.battle_multiplier
                lose_val = -8

            if 800 <= brawler_trophies <= 899:
                win_val = 5 * self.player.battle_multiplier
                lose_val = -9

            if 900 <= brawler_trophies <= 999:
                win_val = 5 * self.player.battle_multiplier
                lose_val = -10

            if 1000 <= brawler_trophies <= 1099:
                win_val = 5 * self.player.battle_multiplier
                lose_val = -11

            if 1100 <= brawler_trophies <= 1199:
                win_val = 4 * self.player.battle_multiplier
                lose_val = -12

            if brawler_trophies >= 1200:
                win_val = 3 * self.player.battle_multiplier
                lose_val = -12
        if self.type == 0:
            if self.result == 0:
                multplier = 1
                if self.player.token_doubler >= 15:
                    multplier = 2
                    self.player.token_doubler = self.player.token_doubler - 15
                    self.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
                else:
                    multplier = 1
                new_trophies = old_tr + win_val
                self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + win_val
            
                self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
                self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)
                self.db.update_player_account(self.player.token, 'Trophies', new_trophies)

                old_res_brawl_box = self.player.resources[0]['Amount']
                old_res_big_box = self.player.resources[2]['Amount']
                self.player.resources[2]['Amount'] = old_res_big_box + 1
                self.player.resources[0]['Amount'] = old_res_brawl_box + 15 * multplier
                self.db.update_player_account(self.player.token, "Resources", self.player.resources)
                #self.writeVInt(15 * multplier)
                #self.writeVInt(win_val)
            else:
                multplier = 1
                if self.player.token_doubler >= 15:
                    multplier = 2
                    self.player.token_doubler = self.player.token_doubler - 15
                    self.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
                else:
                    multplier = 1
                new_trophies = old_tr + lose_val
                self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + lose_val
                self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + lose_val
            
                self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
                self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)
                self.db.update_player_account(self.player.token, 'Trophies', new_trophies)
            
                old_res_brawl_box = self.player.resources[0]['Amount']
                old_res_big_box = self.player.resources[2]['Amount']
                self.player.resources[2]['Amount'] = old_res_big_box + 0
                self.player.resources[0]['Amount'] = old_res_brawl_box + 5 * multplier
                self.db.update_player_account(self.player.token, "Resources", self.player.resources)
                #self.writeVInt(5 * multplier)#токены
                #self.writeVInt(lose_val)#трофеи
        else:
            print("BIM BA< BAM")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0) # Unknown
        self.writeVInt(0) # Doubled Tokens
        self.writeVInt(0) # Double Token Event
        self.writeVInt(0) # Token Doubler Remaining
        self.writeVInt(0) # Championship Lose 
        self.writeVInt(0) # Unknown
        self.writeVInt(0) # Championship Level Passed
        self.writeVInt(0) # Challenge Reward Type (0 = Star Tokens, 1 = Star Tokens)
        self.writeVInt(0) #C hallenge Reward Ammount
        self.writeVInt(0) # Championship Losses Left
        self.writeVInt(0) # Championship Maximun Losses
        self.writeVInt(8) # Coin Shower Event
        self.writeVInt(15) #Underdog (But I Didn't Coded Yet)
        self.writeVInt(50) #Battle Result Type ((-16)-(-1) = Power Play Battle End, 0-15 = Practice and Championship Battle End, 16-31 = Matchmaking Battle End, 32-47 = Friendly Game Battle End, 48-63  = Spectate and Replay Battle End, 64-79 = Championship Battle End)
        self.writeVInt(-64) # Championship Type
        self.writeVInt(0) # Unused Star Token (Beta Brawl Pass Stuff?)

        # Players in Game Array
        self.writeVInt(len(self.players))

        for player in self.players:
            self.brawler  = self.players[player]['Brawler']
            self.skin     = self.players[player]['Skin']
            self.team     = self.players[player]['Team']
            self.username = self.players[player]['Name']


            self.writeDataReference(16, self.brawler)if self.brawler != -1 else self.writeVInt(0) # Player Brawler SCID
            self.writeDataReference(29, self.skin)   if self.skin    != -1 else self.writeVInt(0) # Player Skin SCID

            self.writeVInt(0) # Player Trophies
            self.writeVInt(0) # Player Highest Trophies
            self.writeVInt(10)    # Player Power Level

            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(1)

            self.writeString(self.username) # Player Name

            self.writeVInt(100)      # Unknown
            self.writeVInt(28000000) # Player Profile Icon ID
            self.writeVInt(43000001) # Player Name Color ID
            self.writeVInt(0)


        # Experience Array
        self.writeVInt(2) # Count
        self.writeVInt(0) # Normal Experience ID
        self.writeVInt(1) # Normal Experience Ammount
        self.writeVInt(8) # Star Player Experience ID
        self.writeVInt(2) # Star Player Experience Ammount

        # Rank Up and Level Up Bonus Array
        self.writeVInt(2) # Count
        self.writeVInt(39) # Milestone CsvID
        self.writeVInt(33) # Milestone Row (row 33 is rank 35)
        self.writeVInt(39) # Milestone CsvID
        self.writeVInt(34) # Milestone Row


        # Trophies and Experience Bars Array
        self.writeVInt(2) # Count
        self.writeVInt(1) # Ranks Milestone ID
        self.writeVInt(0) # Brawler Trophies Bar
        self.writeVInt(0) # Brawler Trophies for Rank
        self.writeVInt(5) # Experience Milestone ID
        self.writeVInt(0) # Total Experience Bar
        self.writeVInt(0) # ???
        
        self.writeVInt(0)  # Unknown
        self.writeBoolean(True)  # Play Again
        self.writeVInt(1) # Count

        for x in range(1):
            self.writeVInt(1)

            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeUInt8(0)

            self.writeDataReference(16, 0)

            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            