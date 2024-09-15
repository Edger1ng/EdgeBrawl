from ByteStream.Writer import Writer
import time

class BattleResult2Message(Writer):

    def __init__(self, client, player, db):
        super().__init__(client)
        self.id = 23456
        self.player = player
        self.db = db

    def encode(self):
        brawler_trophies = self.player.brawlers_trophies[str(self.player.home_brawler)]
        brawler_trophies_for_rank = self.player.brawlers_high_trophies[str(self.player.home_brawler)]
        
        if 0 <= brawler_trophies <= 49:
        	win = 8
        	lose = 0
        	draw = 0
        	lose2 = 0


        else:
            if 50 <= brawler_trophies <= 99:
                win = 4
                lose = -1
                draw = 0
                lose2 = -64


            if 100 <= brawler_trophies <= 199:
                win = 6
                lose = -2
                draw = 0
                lose2 = -63


            if 200 <= brawler_trophies <= 299:
                win = 8
                lose = -3
                draw = 0
                lose2 = -62

            	
            if 300 <= brawler_trophies <= 399:
                win = 10
                lose = -4
                draw = 0
                lose2 = -61


            if 400 <= brawler_trophies <= 499:
                win = 12
                lose = -5
                draw = 0
                lose2 = -60

                
            if 500 <= brawler_trophies <= 549:
                win = 14
                lose = -5
                draw = 0
                lose2 = -60
                
            if 550 <= brawler_trophies <= 599:
                win = 16
                lose = -6
                draw = 0
                lose2 = -60

            if 600 <= brawler_trophies <= 649:
                win = 18
                lose = -6
                draw = 0
                lose2 = -59

            if 650 <= brawler_trophies <= 699:
                win = 20
                lose = -6
                draw = 0
                lose2 = -59

                
            if 700 <= brawler_trophies <= 749:
                win = 22
                lose = -20
                draw = 0
                lose2 = -58

            if 750 <= brawler_trophies <= 799:
                win = 24
                lose = -20
                draw = 0
                lose2 = -58

                
            if 800 <= brawler_trophies <= 849:
                win = 24
                lose = -20
                draw = 0
                lose2 = -57

                
            if 850 <= brawler_trophies <= 899:
                win = 24
                lose = -20
                draw = 0
                lose2 = -55

                
            if brawler_trophies >= 900:
                win = 24
                lose = -20
                draw = 0
                lose2 = -53
                
                
            		

        
        if self.player.battle_result == 0:
            multplier = 1
            if self.player.token_doubler >= 200:
                multplier = 2
                self.player.token_doubler = self.player.token_doubler - 200
                self.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
            else:
                multplier = 1
            league_m = 0
            gems = 0
            league_m_trop = 1.00
            if self.player.league == 1:
                if league_m <= 20:
                    league_m = 1.20
                else:
                    pass
                league_m_trop = 1.00
                gems = 0.3
            if self.player.league == 2:
                if league_m <= 30:
                    league_m = 1.30
                else:
                    pass
                league_m_trop = 1.10
                gems = 0.5
            if self.player.league == 3:
                if league_m <= 40:
                     league_m = 1.40
                else:
                     pass
                league_m_trop = 1.20
                gems = 0.7
            if self.player.league == 4:
                if league_m <= 50:
                     league_m = 1.50
                else:
                     pass
                league_m_trop = 1.30
                gems = 0.9
            self.player.league_bank = self.player.league_bank + gems
            self.db.update_player_account(self.player.token, 'LeagueBank', self.player.league_bank)
            if self.player.league_multiplier != 0:
                 if self.player.league_m_time >= int(time.time()):
                      league_multiplier = self.player.league_multiplier / 100
                      league_points = 2 * league_multiplier
                      self.player.league_points = self.player.league_points + league_points
                 else:
                      self.player.league_points = self.player.league_points + 5
            else:
                 self.player.league_points = self.player.league_points + 5
            self.db.update_player_account(self.player.token, 'LeaguePoints', self.player.league_points)
            #self.player.league_points = self.player.league_points + 5
            if league_m != 0:
                league_m = league_m / 100
            else:
                 pass
            trop = win
            tkns = 200 * multplier
            tkns2 = 80 * multplier
            if league_m != 1.00:
                tkns = int(tkns * league_m)
                tkns2 = int(tkns2 * league_m)
            else:
                 pass
            wintr = win * self.player.battle_multiplier
            if league_m_trop != 1.00:
                 wintr = wintr * league_m_trop
            else:
                 pass
            self.player.wins = self.player.wins + 1
            self.player.solo_wins = self.player.solo_wins + 1
            self.db.update_player_account(self.player.token, '3v3Wins', self.player.solo_wins)
            self.db.update_player_account(self.player.token, 'Wins', self.player.wins)
            if self.player.wins == 2:
                 wintr = wintr + 1
            if self.player.wins == 3:
                 wintr = wintr + 2
            if self.player.wins == 4:
                 wintr = wintr + 3
            if self.player.wins == 5:
                 wintr = wintr + 4
            if self.player.wins == 6:
                 wintr = wintr + 5
            if self.player.wins == 7:
                 wintr = wintr + 6
            if self.player.wins == 8:
                 wintr = wintr + 7
            if self.player.wins >= 9:
                 wintr = wintr + 8
            else:
                 pass
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + tkns2
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + tkns
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
            self.player.trophies += wintr
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + wintr
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + wintr
            
            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)

            self.db.update_player_account(self.player.token, 'LeagueBank', self.player.league_bank)
            #old_res_brawl_box = self.player.resources[0]['Amount'] Dont used after 1th Patch
            #old_res_big_box = self.player.resources[2]['Amount'] Dont used after 1th Patch
            #self.player.resources[2]['Amount'] = old_res_big_box + 1 Dont used after 1th Patch
            #self.player.resources[0]['Amount'] = old_res_brawl_box + 15 * multplier Dont used after 1th Patch
            #self.db.update_player_account(self.player.token, "Resources", self.player.resources) Dont used after 1th Patch



        
        elif self.player.battle_result == 1:
            multplier = 1
            if self.player.token_doubler >= 15:
                multplier = 2
                self.player.token_doubler = self.player.token_doubler - 15
                self.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
            else:
                multplier = 1
            league_m = 0
            gems = 0
            league_m_trop = 1.00
            if self.player.league == 1:
                if league_m <= 20:
                    league_m = 1.20
                else:
                    pass
                league_m_trop = 1.00
                gems = 0.1
            if self.player.league == 2:
                if league_m <= 30:
                    league_m = 1.30
                else:
                    pass
                league_m_trop = 1.10
                gems = 0.2
            if self.player.league == 3:
                if league_m <= 40:
                     league_m = 1.40
                else:
                     pass
                league_m_trop = 1.20
                gems = 0.4
            if self.player.league == 4:
                if league_m <= 50:
                     league_m = 1.50
                else:
                     pass
                league_m_trop = 1.30
                gems = 0.6
            self.player.league_bank = self.player.league_bank + gems
            if self.player.league_multiplier != 0:
                 if self.player.league_m_time >= int(time.time()):
                      league_multiplier = self.player.league_multiplier / 100
                      league_points = 2 * league_multiplier
                      self.player.league_points = self.player.league_points + league_points
                 else:
                      self.player.league_points = self.player.league_points + 2
            else:
                 self.player.league_points = self.player.league_points + 2
            self.db.update_player_account(self.player.token, 'LeaguePoints', self.player.league_points)
            #self.player.league_points = self.player.league_points + 2
            trop = win
            tkns = 200 * multplier
            tkns2 = 80 * multplier
            if league_m != 1.00:
                tkns = int(tkns * league_m)
                tkns2 = int(tkns2 * league_m)
            else:
                 pass
            wintr = win * self.player.battle_multiplier
            if league_m_trop != 1.00:
                 losetr =  trop * league_m_trop
            else:
                 pass
            trop = lose
            self.player.trophies += lose
            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + lose
            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + lose
            tkns = 50 * multplier
            tkns2 = 20 * multplier
            if self.player.pass_tokens >= 34500:
                self.player.reserve_tokens = self.player.reserve_tokens + tkns2
                self.db.update_player_account(self.player.token, 'ReserveTokens', self.player.reserve_tokens)
            else:
                self.player.pass_tokens = self.player.pass_tokens + tkns
                self.db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)

            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
            
            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)
            
        self.writeVInt(1)
        self.writeVInt(self.player.battle_result)
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

        self.writeVInt(6) #players count
        
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
        		
        self.writeVInt(0)# Team and Star Player Type
        self.writeVInt(16)
        self.writeVInt(self.player.bot1)# Player Brawler
        
        self.writeVInt(0)
        self.writeVInt(0)# Player Skin
        
        self.writeVInt(0)# Your Brawler Trophies
        self.writeVInt(10)# Your Brawler Power Level
        self.writeVInt(0)# HighID and LowID Array
        self.writeString(self.player.bot1_n)# Your Name
        self.writeVInt(100)# Player Experience Level
        self.writeVInt(28000000)# Player Profile Icon
        self.writeVInt(43000000)# Player Name Color
        self.writeVInt(0)# Player Name Gradient
        		
        		
        		
        self.writeVInt(0)# Team and Star Player Type
        self.writeVInt(16)
        self.writeVInt(self.player.bot2)# Player Brawler
        
        self.writeVInt(0)
        self.writeVInt(0)# Player Skin
        
        self.writeVInt(0)# Your Brawler Trophies
        self.writeVInt(10)# Your Brawler Power Level
        self.writeVInt(0)# HighID and LowID Array
        self.writeString(self.player.bot2_n)# Your Name
        self.writeVInt(100)# Player Experience Level
        self.writeVInt(28000000)# Player Profile Icon
        self.writeVInt(43000000)# Player Name Color
        self.writeVInt(0)# Player Name Gradient
        		
        
        		
        				
        						
        								
        										
        self.writeVInt(2)# Team and Star Player Type
        self.writeVInt(16)
        self.writeVInt(self.player.bot3)# Player Brawler
        
        self.writeVInt(0)
        self.writeVInt(0)# Player Skin
        
        self.writeVInt(0)# Your Brawler Trophies
        self.writeVInt(10)# Your Brawler Power Level
        self.writeVInt(0)# HighID and LowID Array
        self.writeString(self.player.bot3_n)# Your Name
        self.writeVInt(100)# Player Experience Level
        self.writeVInt(28000000)# Player Profile Icon
        self.writeVInt(43000000)# Player Name Color
        self.writeVInt(0)# Player Name Gradient
        
        
        
        		
        self.writeVInt(2)# Team and Star Player Type
        self.writeVInt(16)
        self.writeVInt(self.player.bot4)# Player Brawler
        
        self.writeVInt(0)
        self.writeVInt(0)# Player Skin
        
        self.writeVInt(0)# Your Brawler Trophies
        self.writeVInt(10)# Your Brawler Power Level
        self.writeVInt(0)# HighID and LowID Array
        self.writeString(self.player.bot4_n)# Your Name
        self.writeVInt(100)# Player Experience Level
        self.writeVInt(28000000)# Player Profile Icon
        self.writeVInt(43000000)# Player Name Color
        self.writeVInt(0)# Player Name Gradient
        	
        	
        self.writeVInt(2)# Team and Star Player Type
        self.writeVInt(16)
        self.writeVInt(self.player.bot5)# Player Brawler
        
        self.writeVInt(0)
        self.writeVInt(0)# Player Skin
        
        self.writeVInt(0)# Your Brawler Trophies
        self.writeVInt(10)# Your Brawler Power Level
        self.writeVInt(0)# HighID and LowID Array
        self.writeString(self.player.bot5_n)# Your Name
        self.writeVInt(100)# Player Experience Level
        self.writeVInt(28000000)# Player Profile Icon
        self.writeVInt(43000000)# Player Name Color
        if 1 == 1:
        	self.writeVInt(42000000 + 0) # Gradient Name (42)
        else:
        		self.writeVInt(0) # Gradient Name (42)
        		
        		
        		brawler_trophies = self.player.brawlers_trophies[str(self.player.home_brawler)]
        brawler_high = self.player.brawlers_high_trophies[str(self.player.home_brawler)]
        # Experience Array
        self.writeVInt(2) # Count
        self.writeVInt(0) # Normal Experience ID
        self.writeVInt(0) # Normal Experience Gained
        
        self.writeVInt(8) # Star Player Experience ID
        self.writeVInt(1) # Star Player Experience Gained

        # Rank Up and Level Up Bonus Array
        self.writeVInt(0) # Count

        # Trophies and Experience Bars Array
        self.writeVInt(2) # Count
        self.writeVInt(1) # Trophies Bar Milestone ID
        self.writeVInt(brawler_trophies - trop) # Brawler Trophies
        self.writeVInt(brawler_trophies_for_rank - trop) # Brawler Trophies for Rank
        
        self.writeVInt(5) # Experience Bar Milestone ID
        self.writeVInt(self.player.exp_points) # Player Experience
        self.writeVInt(self.player.exp_points) # Player Experience for Level

        self.writeDataReference(28, 0)

        self.writeBool(False)