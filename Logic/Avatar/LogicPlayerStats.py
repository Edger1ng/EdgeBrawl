class LogicPlayerStats:

    def getPlayerStats(self, accountData):

        playerStats = {

            '3v3Victories': accountData['3v3Wins'],
            'ExperiencePoints': accountData['ExperiencePoints'],
            'Trophies': accountData['Trophies'],
            'HighestTrophies': accountData['HighestTrophies'],
            'UnlockedBrawlersCount': len(accountData['UnlockedBrawlers']),
            'Unknown2': 0,
            'ProfileIconID': 28000000 + accountData['ProfileIcon'],
            'SoloVictories': accountData['SoloWins'],
            'HighestRoboRumbleLvlPassed': 21,
            'Unknown3': 0,
            'DuoVictories': 0,
            'HighestBossFightLvlPassed': 21,
            'Unknown4': 0,
            'PowerPlayRank': accountData['LeaguePoints'],
            'MostChallengeWins': accountData['EventPoints'],
            'HighestRampageLvlPassed': 21

        }

        return playerStats
