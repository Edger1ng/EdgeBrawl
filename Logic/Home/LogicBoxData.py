import random
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage


class LogicBoxData:

    def randomize(self, type):
        self.box_rewards = { 'Rewards': [] }

        if (type == 10):
            rarity = random.randint(0,100)
            check = False
            if (rarity in range(1, 40)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(50, 500)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    gold_value = 750
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 10
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 20
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(41, 65)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(250, 750)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    gold_value = 1000
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 20
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 10
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(66, 85)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(500, 1500)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                    if (locked_brawlers):
                        brawler = random.choice(locked_brawlers)
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)
                        if brawler not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    else:
                        gold_value = random.randint(1000, 2000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 15
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 25
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(86, 95)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(1500, 4000)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                    if (locked_brawlers):
                        brawler = random.choice(locked_brawlers)
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)
                        if brawler not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    else:
                        gold_value = random.randint(2000, 5000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 25
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 50
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(96, 100)):
                reward = random.randint(1, 4)
                if (reward == 1):
                    gold_value = random.randint(1000, 6000)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                    if (locked_brawlers):
                        brawler = random.choice(locked_brawlers)
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)
                        if brawler not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    else:
                        gold_value = random.randint(5000, 10000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 50
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 80
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)







        elif (type == 12):
            rarity = random.randint(0,100)
            check = False
            if (rarity in range(1, 20)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(50, 500)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    gold_value = 750
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 10
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 20
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(21, 60)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(250, 750)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    gold_value = 1000
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 20
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 10
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(61, 85)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(500, 1500)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                    if (locked_brawlers):
                        brawler = random.choice(locked_brawlers)
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)
                        if brawler not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    else:
                        gold_value = random.randint(1000, 2000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 15
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 25
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(86, 95)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(1500, 4000)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                    if (locked_brawlers):
                        brawler = random.choice(locked_brawlers)
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)
                        if brawler not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    else:
                        gold_value = random.randint(2000, 5000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 25
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 50
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(96, 100)):
                reward = random.randint(1, 4)
                if (reward == 1):
                    gold_value = random.randint(1000, 6000)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                    if (locked_brawlers):
                        brawler = random.choice(locked_brawlers)
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)
                        if brawler not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    else:
                        gold_value = random.randint(5000, 10000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 50
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 80
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)


        elif (type == 11):
            rarity = random.randint(0,100)
            check = False
            if (rarity in range(1, 15)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(50, 500)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    gold_value = 750
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 10
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 20
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(16, 35)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(250, 750)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    gold_value = 1000
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 20
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 10
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(36, 75)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(500, 1500)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                    if (locked_brawlers):
                        brawler = random.choice(locked_brawlers)
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)
                        if brawler not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    else:
                        gold_value = random.randint(1000, 2000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 15
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 25
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(76, 90)):
                reward = random.randint(1,4)
                if (reward == 1):
                    gold_value = random.randint(1500, 4000)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                    if (locked_brawlers):
                        brawler = random.choice(locked_brawlers)
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)
                        if brawler not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    else:
                        gold_value = random.randint(2000, 5000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    gems_value = 25
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
                elif (reward == 4):
                    gems_value = 50
                    self.player.gems = self.player.gems + gems_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                    gems_reward = {'Amount': gems_value, 'DataRef': [0, 0], 'Value': 8}
                    self.box_rewards['Rewards'].append(gems_reward)
            elif (rarity in range(91, 100)):
                reward = 4 #random.randint(1, 4)
                if (reward == 1):
                    gold_value = random.randint(1000, 6000)
                    gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                    self.box_rewards['Rewards'].append(gold_reward)
                    self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                    self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 2):
                    locked_brawlers = sorted(set(self.player.brawlers_id) - set(self.player.brawlers_unlocked))
                    if (locked_brawlers):
                        brawler = random.choice(locked_brawlers)
                        brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Value': 1}
                        self.box_rewards['Rewards'].append(brawler_reward)
                        if brawler not in self.player.brawlers_unlocked:
                            self.player.brawlers_unlocked.append(brawler)
                            self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
                    else:
                        gold_value = random.randint(5000, 10000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 3):
                    locked_skins = sorted(set(self.player.skins_id) - set(self.player.unlocked_skins))
                    if (locked_skins):
                        skin = random.choice(locked_skins)
                        skin_reward = {'Amount': 1, 'DataRef': [29, skin], 'Value': 9}
                        self.box_rewards['Rewards'].append(skin_reward)
                        print("HUI HUI SKIN!!!!")
                        if skin not in self.player.unlocked_skins:
                            print("HUIHUI SKIN!!!!!@222")
                            self.player.unlocked_skins.append(skin)
                            self.player.db.update_player_account(self.player.token, 'UnlockedSkins', self.player.unlocked_skins)
                            self.player.err_code = 1
                            LoginFailedMessage(self.client, self.player, f'Поздравляю!Вам выпал скин!\nID скина: {skin}\nВаш ID: {self.player.id}\n(Иногда нужно поддержке)').send()
                    else:
                        gold_value = random.randint(5000, 10000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                elif (reward == 4):
                    locked_skins = sorted(set(self.player.skins_id) - set(self.player.unlocked_skins))
                    if (locked_skins):
                        skin = random.choice(locked_skins)
                        skin_reward = {'Amount': 1, 'DataRef': [29, skin], 'Value': 9}
                        self.box_rewards['Rewards'].append(skin_reward)
                        print("HUI HUI SKIN!!!!")
                        if skin not in self.player.unlocked_skins:
                            print("HUIHUI SKIN!!!!!@222")
                            self.player.unlocked_skins.append(skin)
                            self.player.db.update_player_account(self.player.token, 'UnlockedSkins', self.player.unlocked_skins)
                            self.player.err_code = 1
                            LoginFailedMessage(self.client, self.player, f'Поздравляю!Вам выпал скин!\nID скина: {skin}\nВаш ID: {self.player.id}\n(Иногда нужно поддержке)').send()
                    else:
                        gold_value = random.randint(5000, 10000)
                        gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Value': 7}
                        self.box_rewards['Rewards'].append(gold_reward)
                        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                        self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)

        return self.box_rewards


