import sys
import datetime
from DataBase.SQLManager import DataBase as dB
from Logic.Player import Player
import json
from Utils.Helpers import Helpers
import os
class DB:
    def __init__(self):
        self.player = Player
        self.client = dB("players.sqlite")
        self.clubs = dB("clubs.sqlite")

        self.data = {
            'Name': 'Guest',
            'Perm': Player.perm,
            'Doubles': Player.doubles,
            'NameSet': False,
            'Gems': Player.gems,
            'Trophies': Player.trophies,
            'Tickets': Player.tickets,
            'Resources': Player.resources,
            'TokenDoubler': 0,
            'HighestTrophies': 0,
            'HomeBrawler': 0,
            'TrophyRoadReward': 300,
            'ExperiencePoints': Player.exp_points,
            'ProfileIcon': 0,
            'NameColor': 0,
            'UnlockedBrawlers': Player.brawlers_unlocked,
            'BrawlersTrophies': Player.brawlers_trophies,
            'BrawlersHighestTrophies': Player.brawlers_high_trophies,
            'BrawlersLevel': Player.brawlers_level,
            'BrawlersPowerPoints': Player.brawlers_powerpoints,
            'UnlockedSkins': Player.unlocked_skins,
            'SelectedSkins': Player.selected_skins,
            'SelectedBrawler': 0,
            'Region': Player.region,
            'SupportedContentCreator': "",
            'StarPower': Player.starpower,
            'Gadget': Player.gadget,
            'BrawlPassActivated': False,
            'WelcomeMessageViewed': False,
            'ClubID': 0,
            'ClubRole': 1,
            'TimeStamp': str(datetime.datetime.now()),
            'Ban': Player.account_ban,
            'BanReason': Player.ban_reason,
            'BanSupport': Player.ban_support,
            'Maintenance': Player.acc_maintenance,
            'MaintenanceType': Player.maintenance_type, #0 - откл, 1 - Текст, 2 - Обычный тех перерыв, 3 - Бан + текст, 4 - перерыв
            'MaintenanceText': Player.maintenance_text,
            'Buyed': Player.buyed,
            'DonateLvl': Player.donateid,
            'BattleMultiplier': Player.battle_multiplier,
            'PremiumActivated': Player.premium,
            'BetaEnabled': Player.beta_enabled,
            'FirstDonate': Player.first_donate,
            'DonateSeason': [0],
            'TempbanDate': "",
            'Notifications': Player.notifications,
            'MultiplierTime': Player.m_time,
            'PassTokens': 1,
            'SeasonProgress': 2,
            'FreePassClaimed': [],
            'DonatePassClaimed': [],
            'ReserveTokens': 0,
            'IsLinked': False,
            'League': 0,
            'LeaguePoints': 0,
            'LeagueMultiplierPercent': 0,
            'LeagueMultiplierTime': 0,
            'LeagueBank': 0,
            'NeedToUpgradeLvl': False,
            'FreezeSecurity': False,
            'FreezeMode': 0,
            'FreezeTime': 0,
            'Airblank': 0
        }

        self.club_data = {
            'Name': '',
            'Description': '',
            'Region': '',
            'BadgeID': 0,
            'Type': 0,
            'Trophies': 0,
            'RequiredTrophies': 0,
            'FamilyFriendly': 0,
            'Members': [],
            'Messages': []
        }

    def merge(self, dict1, dict2):
        return (dict1.update(dict2))


    def create_player_account(self, id, token):
        auth = {
            'ID': id,
            'Token': token,
        }

        auth.update(self.data)
        open("manager.logs", "a").write(f"\nDB: Account created\n{datetime.datetime.now()}:\n{str(id)}\n{str(token)}\n")

        self.client.insert(token, auth)


    def load_player_account(self, id, token):
    	result = self.client.load_data(token)
    	if result:
            for x in self.data:
                if x not in result:
                    result[x] = self.data[x]

            return result
    def load_player_account_by_id(self, id):
    	collections = self.client.load_all()
    	for collection in collections:
    		if collection["ID"] == id:
    			return collection

    def update_player_account(self, token, item, value):
        self.client.update(token, item, value)
        print(f"[DBMANAGER] Updated player {token}, item {item}, value {value}")
        open("manager.logs", "a").write(f"\nDB: Account updated\n{datetime.datetime.now()}:\n{str(token)}, {str(item)}, {str(value)}\n")


    def update_all_players(self, query, item, value):
    	collections = self.client.load_all()
    	for collection in collections:
    		self.client.update(collection["Token"], item, value)

    def update_all_tokens(self):
        collections = self.client.load_all()
        for collection in collections:
            reserve_tokens = collection["ReserveTokens"]
            self.client.update(collection["Token"], "PassTokens", reserve_tokens)

            
    		
    def load_all_players(self, args):
        result = self.client.load_all()
        print(f"[DBMANAGER] Loaded all players {args}")
        return result


    def load_all_players_sorted(self, args, element):
        result = self.client.load_all()
        sorter = sorted(result, key=lambda x:x[element], reverse=True)
        return sorter


    def create_club(self, id, data):
        auth = {
            'ID': id,
        }

        auth.update(data)

        self.clubs.insert(id, auth)
        print(f"[DBMANAGER] Created club {id}, data {data}")


    def update_club(self, id, item, value):
        query = {"ID": id}
        self.clubs.update(id, item, value)


    def load_club(self, id):
        query = {"ID": id}
        result = self.clubs.load_data(id)
        return result


    def load_all_clubs_sorted(self, args, element):
    	result = self.clubs.load_all()
    	sorter = sorted(result, key=lambda x:x[element], reverse=True)
    	return sorter

    def load_all_clubs(self, args):
        result = self.clubs.load_all()
        return result

    def delete_club(self, id):
        query = {"ID": id}
        self.clubs.delete(id)
    def close(self):
    	self.client.close()
    	self.clubs.close()
