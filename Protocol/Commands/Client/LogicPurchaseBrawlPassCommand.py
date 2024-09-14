from ByteStream.Reader import Reader
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage
import time 

class LogicPurchaseBrawlPassCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()

    def process(self, db):
        if self.player.donate_level == 0:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, 'Покупка Brawl Pass недоступна для обычных игроков!\nПожалуйста, купите Edge Pass(Минимум Basic Pass) чтобы продолжить!').send()
        if self.player.donate_level == 1:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, 'Активировация Free Pass произведена успешно!\nВыдано: 500 старпоинтов\n250 гемов\n10% Прогресса\n\nОбратите внимание, что для активации самого Brawl Pass нужно купить минимум Basic Pass!').send()
            self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + 500
            self.player.donate_level = 0
            self.player.gems = self.player.gems + 250
            self.player.pass_tokens = self.player.pass_tokens + 3450
            wow = {"NotifID": 81, "NotifIndex": 0, "NotifRead": "true", "NotifTime": int(time.time()), "Notiftext": f'Привет, {self.player.name}!\nТы успешно активировал Edge Pass(Free Pass\nяНадеюсь, он тебе понравится!\nГлавный разработчик, Microsoft Edge'}
            self.player.notifications["2"] = wow
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
            db.update_player_account(self.player.token, 'DonateLvl', self.player.donate_level)
            db.update_player_account(self.player.token, 'Gems', self.player.gems)
            db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
        if self.player.donate_level == 2:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, 'Активация Lite Pass произведена успешно!\nВыдано: 1340 старпоинтов\n670 гемов\n15% Прогресса\n\nОбратите внимание, что для активации Brawl Pass нужен минимум Basic Pass!').send()
            self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + 1340
            self.player.donate_level = 0
            self.player.gems = self.player.gems + 670
            self.player.pass_tokens = self.player.pass_tokens + 5175
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
            db.update_player_account(self.player.token, 'DonateLvl', self.player.donate_level)
            db.update_player_account(self.player.token, 'Gems', self.player.gems)
            db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
        if self.player.donate_level == 3:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, 'Активация Basic Pass произведена успешно!\nВыдано: 2000 старпоинтов\n1000 гемов\n5% Прогресса\nПремиальные награды Brawl Pass!').send()
            self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + 2000
            self.player.donate_level = 0
            self.player.gems = self.player.gems + 1000
            self.player.bp_activated = True
            self.player.pass_tokens = self.player.pass_tokens + 1775
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
            db.update_player_account(self.player.token, 'DonateLvl', self.player.donate_level)
            db.update_player_account(self.player.token, 'Gems', self.player.gems)
            db.update_player_account(self.player.token, 'BrawlPassActivated', self.player.bp_activated)
            db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
        if self.player.donate_level == 4:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, 'Активация Super Pass произведена успешно!\nВыдано: 3000 старпоинтов\n1500 гемов\n15% Прогресса\nПремиальные награды Brawl Pass!').send()
            self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + 3000
            self.player.donate_level = 0
            self.player.gems = self.player.gems + 1500
            self.player.bp_activated = True
            self.player.pass_tokens = self.player.pass_tokens + 5175
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
            db.update_player_account(self.player.token, 'DonateLvl', self.player.donate_level)
            db.update_player_account(self.player.token, 'Gems', self.player.gems)
            db.update_player_account(self.player.token, 'BrawlPassActivated', self.player.bp_activated)
            db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
        if self.player.donate_level == 5:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, 'Активация Mega Pass произведена успешно!\nВыдано: 4500 старпоинтов\n2250 гемов\n30% Прогресса\nПремиальные награды Brawl Pass!').send()
            self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + 4500
            self.player.donate_level = 0
            self.player.gems = self.player.gems + 2250
            self.player.bp_activated = True
            self.player.pass_tokens = self.player.pass_tokens + 10350
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
            db.update_player_account(self.player.token, 'DonateLvl', self.player.donate_level)
            db.update_player_account(self.player.token, 'Gems', self.player.gems)
            db.update_player_account(self.player.token, 'BrawlPassActivated', self.player.bp_activated)
            db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)
        if self.player.donate_level == 6:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, 'Активация Omega Pass произведена успешно!\nВыдано: 6000 старпоинтов\n3000 гемов\n50% Прогресса\nПремиальные награды Brawl Pass!').send()
            self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + 6000
            self.player.donate_level = 0
            self.player.gems = self.player.gems + 3000
            self.player.bp_activated = True
            self.player.pass_tokens = self.player.pass_tokens + 17250
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
            db.update_player_account(self.player.token, 'DonateLvl', self.player.donate_level)
            db.update_player_account(self.player.token, 'Gems', self.player.gems)
            db.update_player_account(self.player.token, 'BrawlPassActivated', self.player.bp_activated)
            db.update_player_account(self.player.token, 'PassTokens', self.player.pass_tokens)

        