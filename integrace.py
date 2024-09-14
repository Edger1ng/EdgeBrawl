from DataBase.DBManager import DB

db = DB()
a = db.load_all_players_sorted({}, 'Trophies')
print(a)