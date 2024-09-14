from ByteStream.Reader import Reader
from Utils.Helpers import Helpers
from Logic.Home.LogicShopData import LogicShopData
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Logic.LogicBP import LogicBP
from Logic.PinPack import PinPack
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage

class LogicClaimRankUpRewardCommand(Reader):
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.player = player
		self.client = client

	def decode(self):
		self.a = self.readVInt()
		self.b = self.readVInt()
		self.g = self.readVInt()
		self.j = self.readVInt()
		self.bp = self.readVInt()  # 10-free 9-prem
		self.p = self.readVInt()
		self.k = self.readVInt()
		self.id = self.readVInt()  # lvl id bp
		self.id2 = self.readVInt()
		self.obed = self.readVInt()
		self.w = self.readVInt()
		self.hs = self.readVInt()
		self.ks = self.readVInt()
		self.lk = self.readVInt()
		self.fd = self.readVInt()
		self.hd = self.readVInt()
		self.cg = self.readVInt()
		self.jz = self.readVInt()
		
		print(f"{self.a} {self.b} {self.g} {self.j} {self.bp}bp {self.p} {self.k}brawler {self.id}lvl {self.id2}lvl2 {self.obed} {self.w} {self.hs} {self.ks} {self.lk} {self.fd} {self.hd} {self.cg} {self.jz}")

	def process(self, db):
		self.player.delivery_items = {
			'Count': 1,
			'Type': 0,
			'Items': []
		}
		
		if self.id == 0 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(0)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 1 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.delivery_type = 100

		if self.id == 2 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				LogicBP(self.client, self.player, 10, 8, 0, [0, 0], 0).send()
				self.player.gems = self.player.gems + 10
				self.player.delivery_type = 100
				db.update_player_account(self.player.token, 'Gems', self.player.gems)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)

		
		if self.id == 3 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 4 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(4)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 5 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 7 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 8 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 9 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 10 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 11 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 12 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 13 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 14 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				LogicBP(self.client, self.player, 10, 8, 0, [0, 0], 0).send()
				self.player.gems = self.player.gems + 10
				db.update_player_account(self.player.token, 'Gems', self.player.gems)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 15 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 16 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 17 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 18 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				LogicBP(self.client, self.player, 50, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 50
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 19 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 20 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 21 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 22 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				LogicBP(self.client, self.player, 20, 8, 0, [0, 0], 0).send()
				self.player.gems = self.player.gems + 20
				db.update_player_account(self.player.token, 'Gems', self.player.gems)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 23 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 24 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 25 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id2 == 26 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				LogicBP(self.client, self.player, 50, 6, self.k, [0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 50
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 27 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 28 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 29 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 30 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 31 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 32 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 100, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 100
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 33 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id2 == 34 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 50, 6, self.k, [0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 50
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 35 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 36 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 20, 8, 0, [0, 0], 0).send()
				self.player.gems = self.player.gems + 20
				db.update_player_account(self.player.token, 'Gems', self.player.gems)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 37 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 38 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 39 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 40 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 41 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id2 == 42 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 75, 6, self.k, [0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 75
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 43 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 44 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 10, 8, 0, [0, 0], 0).send()
				self.player.gems = self.player.gems + 10
				db.update_player_account(self.player.token, 'Gems', self.player.gems)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 45 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 46 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 47 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 48 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 200, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 200
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 49 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id2 == 50 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 100, 6, self.k, [0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 100
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 51 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 52 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 10, 8, 0, [0, 0], 0).send()
				self.player.gems = self.player.gems + 10
				db.update_player_account(self.player.token, 'Gems', self.player.gems)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 53 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 54 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 55 and self.bp == 10:
			self.player.delivery_items = {'Count': 1, 'Type': 11}
			self.player.bpfree_claimed.append(self.id)
			db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 56 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 200, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 200
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 57 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 58 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 59 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 60 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 61 and self.bp == 10:
			self.player.delivery_items = {'Count': 1, 'Type': 12}
		
		if self.id == 62 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 20, 8, 0, [0, 0], 0).send()
				self.player.gems = self.player.gems + 10
				db.update_player_account(self.player.token, 'Gems', self.player.gems)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 63 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 10}
		
		if self.id2 == 64 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
			else:
				LogicBP(self.client, self.player, 100, 6, self.k, [0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 100
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
		
		if self.id == 65 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 66 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 67 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 500, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 500
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 68 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id2 == 69 and self.bp == 10:
			if self.id in self.player.bpfree_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Вы уже забирали данную награду').send()
			else:
				LogicBP(self.client, self.player, 500, 6, self.k,[0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 500
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
				self.player.bpfree_claimed.append(self.id)
				db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
		
		if self.id == 70 and self.bp == 10:
			import random
			PinPack(self.client, self.player, 0).send()
			self.player.bpfree_claimed.append(self.id)
			db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)

		if self.id == 0 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 1, 9, 0, [29, 204], 0).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 1 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 2 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 100, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 100
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 3 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 4 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 100, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 100
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id2 == 6 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 50, 6, self.k, [0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 50
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 7 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 8 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 100, 7, self.k, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 100
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 9 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 10 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 100, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 100
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 11 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 444).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id2 == 12 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 100, 6, self.k, [0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 100
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 13 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 14 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 200, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 200
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 15 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 444).send()
				self.player.delivery_type = 100
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 16 and self.bp == 9: # pin (439)?
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 441).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 17 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 18 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 444).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 19 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 20 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 21 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 440).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id2 == 22 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 100, 6, self.k, [0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 100
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 23 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 200, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 200
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 24 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 446).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 25 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 26 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 27 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 442).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id2 == 28 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 200, 6, self.k, [0, 0], 0).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 29 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 30 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 443).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 31 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 32 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 33 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 445).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 34 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 200, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 200
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 35 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 515).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 36 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 37 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 516).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id2 == 38 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 200, 6, self.k, [0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 200
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 39 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 520).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 40 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 41 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 518).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 42 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 11}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 43 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 524).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 44 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				self.player.delivery_items = {'Count': 1, 'Type': 12}
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 45 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 517).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 46 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 300, 7, 0, [0, 0], 0).send()
				self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 300
				db.update_player_account(self.player.token, 'Resources', self.player.resources)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 47 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 519).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id2 == 48 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 500, 6, self.k, [0, 0], 0).send()
				self.player.brawlers_powerpoints[str(self.k)] = self.player.brawlers_powerpoints[str(self.k)] + 500
				db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 49 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				PinPack(self.client, self.player, 521).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
		
		if self.id == 50 and self.bp == 9:
			if self.id in self.player.bpdonate_claimed:
				self.player.err_code = 1
				LoginFailedMessage(self.client, self.player, 'Ты уже забрал эту награду!').send()
			else:
				LogicBP(self.client, self.player, 1, 9, 0, [29, 206], 0).send()
				self.player.bpdonate_claimed.append(self.id)
				db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)

		if self.bp == 100:
			if self.bp == 9:
				if self.id not in self.player.bpdonate_claimed:
					self.player.bpdonate_claimed.append(self.id)
					db.update_player_account(self.player.token, 'DonatePassClaimed', self.player.bpdonate_claimed)
			else:
				print("No!")

			if self.bp == 10:
				if self.id in self.player.bpfree_claimed:
					pass
				else:
					self.player.bpfree_claimed.append(self.id)
					db.update_player_account(self.player.token, 'FreePassClaimed', self.player.bpfree_claimed)
			else:
				print("Mister fish!")
			

		self.player.db = db
		AvailableServerCommandMessage(self.client, self.player, 203).send()
		db.load_player_account(self.player.ID, self.player.token)
 