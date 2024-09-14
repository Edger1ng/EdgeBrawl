from ByteStream.Writer import Writer


class BattleResultMessage(Writer):

    def __init__(self, client, player, db):
        super().__init__(client)
        self.id = 23456
        self.player = player
        self.db = db
        
    def encode(self):
        brawler_trophies = self.player.brawlers_trophies[str(self.player.home_brawler)]
        brawler_trophies_for_rank = self.player.brawlers_high_trophies[str(self.player.home_brawler)]
        
        if 0 <= brawler_trophies <= 49:
            rank_0 = 5
            rank_1 = 5
            rank_2 = 4
            rank_3 = 3
            rank_4 = 3
            rank_5 = 2
            rank_6 = 2
            rank_7 = 1
            rank_8 = 1
            rank_9 = 1
            rank_10 = 0

        else:
            if 50 <= brawler_trophies <= 99:
                rank_0 = 6
                rank_1 = 6
                rank_2 = 5
                rank_3 = 4
                rank_4 = 3
                rank_5 = 2
                rank_6 = 1
                rank_7 = 1
                rank_8 = 1
                rank_9 = -1
                rank_10 = -2

            if 100 <= brawler_trophies <= 199:
                rank_0 = 8
                rank_1 = 8
                rank_2 = 6
                rank_3 = 5
                rank_4 = 4
                rank_5 = 3
                rank_6 = 2
                rank_7 = -1
                rank_8 = -2
                rank_9 = -2
                rank_10 = -3

            if 200 <= brawler_trophies <= 299:
                rank_0 = 10
                rank_1 = 10
                rank_2 = 8
                rank_3 = 6
                rank_4 = 4
                rank_5 = 3
                rank_6 = 1
                rank_7 = -1
                rank_8 = -2
                rank_9 = -2
                rank_10 = -4

            if 300 <= brawler_trophies <= 399:
                rank_0 = 12
                rank_1 = 12
                rank_2 = 10
                rank_3 = 8
                rank_4 = 6
                rank_5 = 4
                rank_6 = 2
                rank_7 = 0
                rank_8 = -2
                rank_9 = -4
                rank_10 = -6

            if 400 <= brawler_trophies <= 499:
                rank_0 = 14
                rank_1 = 14
                rank_2 = 12
                rank_3 = 9
                rank_4 = 7
                rank_5 = 5
                rank_6 = 2
                rank_7 = -3
                rank_8 = -4
                rank_9 = -5
                rank_10 = -7

            if 500 <= brawler_trophies <= 549:
                rank_0 = 16
                rank_1 = 16
                rank_2 = 13
                rank_3 = 12
                rank_4 = 10
                rank_5 = 8
                rank_6 = -2
                rank_7 = -3
                rank_8 = -4
                rank_9 = -5
                rank_10 = -5
                
            if 550 <= brawler_trophies <= 599:
                rank_0 = 18
                rank_1 = 18
                rank_2 = 16
                rank_3 = 13
                rank_4 = 11
                rank_5 = 9
                rank_6 = -3
                rank_7 = -4
                rank_8 = -5
                rank_9 = -6
                rank_10 = -7
                
            if 600 <= brawler_trophies <= 649:
                rank_0 = 19
                rank_1 = 19
                rank_2 = 14
                rank_3 = 12
                rank_4 = 10
                rank_5 = 0
                rank_6 = -3
                rank_7 = -5
                rank_8 = -8
                rank_9 = -11
                rank_10 = -13
                
            if 650 <= brawler_trophies <= 699:
                rank_0 = 21
                rank_1 = 21
                rank_2 = 16
                rank_3 = 14
                rank_4 = 12
                rank_5 = -2
                rank_6 = -5
                rank_7 = -8
                rank_8 = -10
                rank_9 = -13
                rank_10 = -15
                
            if 700 <= brawler_trophies <= 749:
                rank_0 = 22
                rank_1 = 22
                rank_2 = 17
                rank_3 = 15
                rank_4 = 13
                rank_5 = -4
                rank_6 = -7
                rank_7 = -10
                rank_8 = -13
                rank_9 = -15
                rank_10 = -18
                
            if 750 <= brawler_trophies <= 799:
                rank_0 = 24
                rank_1 = 24
                rank_2 = 19
                rank_3 = 17
                rank_4 = 0
                rank_5 = -7
                rank_6 = -10
                rank_7 = -13
                rank_8 = -16
                rank_9 = -18
                rank_10 = -21
                
            if 800 <= brawler_trophies <= 849:
                rank_0 = 25
                rank_1 = 25
                rank_2 = 24
                rank_3 = 22
                rank_4 = -4
                rank_5 = -11
                rank_6 = -14
                rank_7 = -17
                rank_8 = -19
                rank_9 = -21
                rank_10 = -24

            if 850 <= brawler_trophies <= 899:
                rank_0 = 26
                rank_1 = 26
                rank_2 = 25
                rank_3 = 23
                rank_4 = -7
                rank_5 = -14
                rank_6 = -17
                rank_7 = -20
                rank_8 = -22
                rank_9 = -24
                rank_10 = -27
                
            if 900 <= brawler_trophies <= 949:
                rank_0 = 26
                rank_1 = 26
                rank_2 = 25
                rank_3 = 23
                rank_4 = -7
                rank_5 = -14
                rank_6 = -17
                rank_7 = -20
                rank_8 = -22
                rank_9 = -24
                rank_10 = -27
                
            if 950 <= brawler_trophies <= 999:
                rank_0 = 26
                rank_1 = 26
                rank_2 = 25
                rank_3 = 23
                rank_4 = -7
                rank_5 = -14
                rank_6 = -17
                rank_7 = -20
                rank_8 = -22
                rank_9 = -24
                rank_10 = -27

            if 1000 <= brawler_trophies <= 1199:
                rank_0 = 26
                rank_1 = 26
                rank_2 = 25
                rank_3 = 23
                rank_4 = -7
                rank_5 = -14
                rank_6 = -17
                rank_7 = -20
                rank_8 = -22
                rank_9 = -24
                rank_10 = -27
                
            if 1200 <= brawler_trophies <= 1249:
                rank_0 = 26
                rank_1 = 26
                rank_2 = 25
                rank_3 = 23
                rank_4 = -7
                rank_5 = -14
                rank_6 = -17
                rank_7 = -20
                rank_8 = -22
                rank_9 = -24
                rank_10 = -27
                
                
            if brawler_trophies >= 1250:
                rank_0 = 26
                rank_1 = 26
                rank_2 = 25
                rank_3 = 23
                rank_4 = -7
                rank_5 = -14
                rank_6 = -17
                rank_7 = -20
                rank_8 = -22
                rank_9 = -24
                rank_10 = -27
                
        if self.player.rank == 1:
            trop = rank_1
            self.player.trophies += trop
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_0
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + rank_0
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + 80
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + 200
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)


        	
        elif self.player.rank == 2:
            trop = rank_2
            self.player.trophies += trop
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + 72
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + 180
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)



        elif self.player.rank == 3:
            trop = rank_3
            self.player.trophies += trop
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + 64
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + 160
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)

            
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)


        	
        elif self.player.rank == 4:
            trop = rank_4
            self.player.trophies += trop
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + 56
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + 140
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
            
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)


        	
        elif self.player.rank == 5: #-
            trop = rank_5
            self.player.trophies += trop
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + 48
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + 120
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)

            
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)


        	
        elif self.player.rank == 6:
            trop = rank_6
            self.player.trophies += trop
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + 40
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + 100
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)


        	
        elif self.player.rank == 7:
            trop = rank_7
            self.player.trophies += trop
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + 32
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + 80
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)


        	
        elif self.player.rank == 8:
            trop = rank_8
            self.player.trophies += trop
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + 24
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + 60
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)

        	
        elif self.player.rank == 9:
            trop = rank_9
            self.player.trophies += trop
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + 16
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + 40
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)

        elif self.player.rank == 10:
            trop = rank_10
            self.player.trophies += trop
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + trop
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + 8
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + 20
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
            self.player.resources[2]['Amount'] = self.player.resources[2]['Amount'] + 0
            self.player.resources[0]['Amount'] = self.player.resources[0]['Amount'] + 0
            self.db.update_player_account(self.player.token, "Resources", self.player.resources)
            
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)
        
        self.writeVInt(2)
        self.writeVInt(self.player.rank)
        
        
        self.writeVInt(0)
        self.writeVInt(trop)#trp

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
        self.writeVInt(0)
        self.writeVInt(0)# coin event

        self.writeVInt(0)# trp2
        self.writeVInt(16)
        self.writeVInt(-64)
        self.writeVInt(1)

        self.writeVInt(1) #players count
        
        self.writeVInt(1) # Team and Star Player Type
        self.writeDataReference(16, self.player.home_brawler) # Player Brawler
        self.writeDataReference(29, self.player.selected_skins[str(self.player.home_brawler)]) # Player Skin
        self.writeVInt(self.player.brawlers_trophies[str(self.player.home_brawler)]) # Your Brawler Trophies
        self.writeVInt(0) # Your Power Play Points
        self.writeVInt(10) # Your Brawler Power Level
        self.writeBoolean(True) # HighID and LowID Array
        self.writeInt(0) # HighID
        self.writeInt(self.player.ID) # LowID
        self.writeString(self.player.name) # Your Name
        self.writeVInt(1) # Player Experience Level
        self.writeVInt(28000000 + 0) # Player Profile Icon
        self.writeVInt(43000000 + self.player.name_color) # Player Name Color
        if self.player.bp_activated == True:
        	self.writeVInt(42000000 + self.player.name_color) # Gradient Name (42)
        else:
        		self.writeVInt(0) # Gradient Name (42)
        		
        		brawler_trophies = self.player.brawlers_trophies[str(self.player.home_brawler)]
        brawler_high = self.player.brawlers_high_trophies[str(self.player.home_brawler)]
        # Experience Array
        self.writeVInt(2) # Count
        self.writeVInt(0) # Normal Experience ID
        self.writeVInt(0) # Normal Experience Gained
        self.writeVInt(8) # Star Player Experience ID
        self.writeVInt(0) # Star Player Experience Gained

        # Rank Up and Level Up Bonus Array
        self.writeVInt(0) # Count

        # Trophies and Experience Bars Array
        self.writeVInt(2) # Count
        self.writeVInt(1) # Trophies Bar Milestone ID
        self.writeVInt(brawler_trophies - trop) # Brawler Trophies
        self.writeVInt(brawler_trophies_for_rank - trop) # Brawler Trophies for Rank
        self.writeVInt(5) # Experience Bar Milestone ID
        self.writeVInt(1) # Player Experience
        self.writeVInt(1) # Player Experience for Level
        
        self.writeDataReference(28, 0)  # Player Profile Icon
        self.writeBoolean(False)  # Play Again