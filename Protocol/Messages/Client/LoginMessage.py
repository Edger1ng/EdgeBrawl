from threading import Timer
import time
from collections import defaultdict
from ByteStream.Reader import Reader
from Utils.Helpers import Helpers
from Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Protocol.Messages.Server.MyAllianceMessage import MyAllianceMessage
from Protocol.Messages.Server.AllianceStreamMessage import AllianceStreamMessage

MAX_PACKETS_PER_IP = 10

class LoginMessage(Reader):
    ip_packet_counts = defaultdict(int)

    @staticmethod
    def reset_packet_count(ip):
        LoginMessage.ip_packet_counts[ip] = 0
        Timer(300, LoginMessage.reset_packet_count, args=[ip]).start()

    def __init__(self, client, player, initial_bytes, ip_address):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.helpers = Helpers()
        self.ip_address = ip_address[0]  # Используем только IP-адрес, игнорируя порт

    def decode(self):
        self.account_id = self.readLong()
        self.account_token = self.readString()
        self.game_major = self.readInt()
        self.game_minor = self.readInt()
        self.game_build = self.readInt()
        self.fingerprint_sha = self.readString()

    def process(self, db):
        print(self.game_major)
        print(self.game_minor)
        print(self.game_build)
        print(self.game_major,  self.game_build)
        self.ip_packet_counts[self.ip_address] += 1
        print(f'{self.ip_packet_counts}')

        if (self.game_major != 28):
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, 'Отличные новости!Доступно обновление на версию: Лето с монстрами!\n\nОбновите Edge Brawl чтобы продолжить игру').send()


        if self.ip_packet_counts[self.ip_address] > MAX_PACKETS_PER_IP:
            self.player.err_code = 11
            LoginFailedMessage(self.client, self.player, f'Слишком много попыток зайти на сервер с вашего IP\nНаша система автоматически ограничила вход с вашего IP на 5 минут\n\nThere are too many attempts to log into the server from your IP\nOur system has automatically limited login from your IP for 5 minutes').send()

        if not hasattr(LoginMessage.reset_packet_count, f"timer_{self.ip_address}"):
            setattr(LoginMessage.reset_packet_count, f"timer_{self.ip_address}", Timer(300, LoginMessage.reset_packet_count, args=[self.ip_address]))
            getattr(LoginMessage.reset_packet_count, f"timer_{self.ip_address}").start()

        if self.ip_address.startswith('91'):
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, f'Наша система заметила что вы заходите с таджикистанского IP\nИз-за этого, продолжение игры невозможно\nПодробней: https://t.me/EdgeBrawl/928 \nIP: {self.ip_address} \n ====\n Our system has noticed that you are logging in from a Tajikistan IP\nBecause of this, it is impossible to continue the game\nMore details:https://t.me/EdgeBrawl/928 \n IP: {self.ip_address}')

        #if self.player.maintenance_old:
            #self.player.err_code = 10
            #LoginFailedMessage(self.client, self.player, '').send()

        if self.fingerprint_sha != self.player.patch_sha and self.player.patch:
            self.player.err_code = 7
            LoginFailedMessage(self.client, self.player, "").send()

        if self.account_id == 0:
            self.player.ID = self.helpers.randomID()
            self.player.token = self.helpers.randomToken()
            print("Token create started")
            try:
                action = db.load_player_account(self.player.ID, self.player.token)
            except IndexError:
                action = None 
            if action == None:
                db.create_player_account(self.player.ID, self.player.token)
            else:
                self.player.ID = 0
                self.player.token = "0"
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, 'Нам не удалось создать ваш аккаунт.Повторите вход через минуту').send()
                print("Antitoken applied")

        else:
            self.player.ID = self.account_id
            self.player.token = self.account_token
            print(self.player.ID, self.player.token)
            player_data = db.load_player_account(self.player.ID, self.player.token)
            if player_data:
                Helpers.load_account(self, player_data)
                if self.player.account_ban == True:
                    if self.player.ban_support == True:
                        self.player.err_code = 11
                        LoginFailedMessage(self.client, self.player, f'Сожалеем...\nВаш аккаунт был заблокирован!\nПричина: {self.player.ban_reason}\n\nВаш ID: {self.player.ID}\nЭтот бан можно оспорить: @edgering').send()
                    else:
                        self.player.err_code = 11
                        LoginFailedMessage(self.client, self.player, f'Сожалеем...\nВаш аккаунт был заблокирован навсегда!\nПричина: {self.player.ban_reason}\n\nВаш ID: {self.player.ID}\nВы не можете оспорить данную блокировку.').send()
                if self.player.maintenance == True and self.player.maintenance_type != 0:
                    if self.player.maintenance_type == 1:
                        self.player.err_code = 1
                        LoginFailedMessage(self.client, self.player, f'Уважаемый {self.player.name},\nВаш аккаунт был заморожен поддержкой!\nПаниковать не зачем, его можно разморозить!\nОбычно это проходит в 72 часах, смотря от ситуации\n\nВаш ID: {self.player.ID}\nКоментарий: {self.player.maintenance_text}').send()
                    if self.player.maintenance_type == 2:
                        self.player.err_code = 10
                        LoginFailedMessage(self.client, self.player, '').send()
                    if self.player.maintenance_type == 3:
                        self.player.err_code = 11
                        LoginFailedMessage(self.client, self.player, f'Уважаемый {self.player.name},\nВаш аккаунт был заморожен поддержкой!\nПаниковать не зачем, его можно разморозить!\nОбычно это проходит в 72 часах, смотря от ситуации\n\nВаш ID: {self.player.ID}\nКоментарий: {self.player.maintenance_text}').send()
                    if self.player.maintenance_type == 4:
                        self.player.err_code = 1
                        LoginFailedMessage(self.client, self.player, f'Уважаемый {self.player.name},\nСервер находится в режиме технического обслуживания!\nПримерное время технических работ: {self.player.maintenance_time}\n\nПодробную информацию вы можете узнать в Telegram канале @EdgeBrawl').send()
                    if self.player.maintenance_type == 5:
                        self.player.err_code = 1
                        LoginFailedMessage(self.client, self.player, 'Ваш аккаунт был удален с помощью системы Edge Connect.')
                if "1" not in self.player.notifications:
                    #self.player.err_code = 1
                    #LoginFailedMessage(self.client, self.player, f'Упс!\nНам потребовалось обновить данные о твоем аккаунте.Пожалуйста, нажми "Ок" и перезайди в игру!').send()
                    wow = {"NotifID": 81, "NotifIndex": 0, "NotifRead": "true", "NotifTime": int(time.time()), "Notiftext": f'Твой ID: {self.player.ID}\nТвой TOKEN: {self.player.token}\n\nНикому не давай их!'}
                    self.player.notifications["1"] = wow
                    db.update_player_account(self.player.token, 'Notifications', self.player.notifications)
                if '38' not in self.player.brawlers_trophies:
                    self.player.brawlers_trophies['38'] = 0
                    self.player.brawlers_high_trophies['38'] = 0
                    self.player.brawlers_level['38'] = 0
                    self.player.brawlers_powerpoints['38'] = 0
                    self.player.selected_skins['38'] = 0
                    db.update_player_account(self.player.token,  'BrawlersTrophies', self.player.brawlers_trophies)
                    db.update_player_account(self.player.token,  'BrawlersHighestTrophies', self.player.brawlers_high_trophies)
                    db.update_player_account(self.player.token,  'BrawlersLevel', self.player.brawlers_level)
                    db.update_player_account(self.player.token,  'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                    db.update_player_account(self.player.token,  'SelectedSkins', self.player.selected_skins)
                    self.player.err_code = 1
                    LoginFailedMessage(self.client, self.player,  'Привет!\nНе бойся, это не блокировка, мы всего лишь должны обновить твой аккаунт чтобы добавить возможность играть на Вольте!').send()
                if self.player.club_id != 0:
                	club_data = db.load_club(self.player.club_id)
                	Helpers.load_club(self, club_data)
                if self.player.m_time <= int(time.time()):
                    self.player.battle_multiplier = 1
                    db.update_player_account(self.player.token, 'BattleMultiplier', self.player.battle_multiplier)
                if self.player.league_points != 0:
                    if self.player.league_points >= 50:
                        if self.player.league >= 1:
                            pass
                        else:
                            db.update_player_account(self.player.token, 'League', 1)
                    if self.player.league_points >= 200:
                        if self.player.league >= 2:
                            pass
                        else:
                            db.update_player_account(self.player.token, 'League', 2)
                    if self.player.league_points >= 400:
                        if self.player.league >= 3:
                            pass
                        else:
                            db.update_player_account(self.player.token, 'League', 3)
                    if self.player.league_points >= 800:
                        if self.player.league >= 4:
                            pass
                        else:
                            db.update_player_account(self.player.token, 'League', 4)
                if self.player.freeze_security:
                    ftime = self.player.freeze_time
                    if self.player.freeze_mode == 1:
                        self.player.err_code == 11
                        LoginFailedMessage(self.client, self.player, f'Данный аккаунт был заморожен через бота управления аккаунтом.Он будет снова разблокирован: {ftime}\nЕсли это были не вы, напишите @edgebrawls')
                    if self.player.freeze_mode == 2:
                        self.player.err_code == 11
                        LoginFailedMessage(self.client, self.player, 'Данный аккаунт был заморожен через бота управления аккаунтом.Он не будет разблокирован, пока это не будет сделано в боте, или инициировано поддержкой\nЕсли это были не вы, напишите @edgebrawls')
                    if self.player.freeze_mode == 3:
                        self.player.err_code == 11
                        LoginFailedMessage(self.client, self.player, 'Данный аккаунт был заморожен через бота управления аккаунтом.Поддержка уже занимается вашим делом.')
                if self.player.needupdate == True:
                    league_points = 0
                    trop = self.player.trophies
                    trop = trop / 2
                    db.update_player_account(self.player.token, 'LeaguePoints', trop)
                    self.player.err_code = 1
                    LoginFailedMessage(self.client, self.player, f'Привет!\nВышло обновление 5.0, связанное с лигами!Ты получил {trop} жетонов лиги!')
                else:
                    pass
            else:
                db.create_player_account(self.player.ID, self.player.token)
                #self.player.err_code = 1
                #LoginFailedMessage(self.client, self.player, "Account not found in database!\nPlease clear app data.").send()

        LoginOkMessage(self.client, self.player, self.player.ID, self.player.token).send()
        OwnHomeDataMessage(self.client, self.player).send()

        if self.player.club_id != 0:
            club_data = db.load_club(self.player.club_id)
            MyAllianceMessage(self.client, self.player, club_data).send()
            AllianceStreamMessage(self.client, self.player, club_data['Messages']).send()
