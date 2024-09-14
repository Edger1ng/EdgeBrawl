import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import CallbackQuery
from aiogram.filters.command import Command
from DataBase.DBManager import DB
import time

TOKEN="7024035753:AAEBoXGer2tVs5bwrjafV7NUkw978Gnh-H0"
bot = Bot(token=TOKEN)
admin_ids = [2128436782, 7011412420]
db = DB()
dp = Dispatcher()


@dp.message(Command('start'))
async def start_handler(message: types.Message):

    if int(message.from_user.id) in admin_ids:
        await message.reply("Привет, мой пупсик.Ты должен прислать мне сообщения типа:\n/update arg1 arg2 arg3\n/info arg1")
    else:
        await message.reply("Ты кто!")

@dp.message(Command('update'))
async def update_handler(message: types.Message):
    if int(message.from_user.id) in admin_ids:
        arg1 = str(message.text.split(' ')[1])
        arg2 = str(message.text.split(' ')[2])
        arg3 = message.text.split(' ')[3]
        arg4 = message.text.split(' ')[4]
        
        if arg4 == "int":
            db.update_player_account(arg1, arg2, int(arg3))
        if arg4 == "bool":
            if arg3 == "False":
                db.update_player_account(arg1, arg2, False)
            if arg3 == "True":
                db.update_player_account(arg1, arg2, True)
        if arg4 == "str":
            db.update_player_account(arg1, arg2, str(arg3))
        await message.reply(f"Upd Player Account:\n{arg1}\n{arg2}\n{arg3}")
    else:
        await message.reply("Я тя не знаю, бро")


@dp.message(Command('info'))
async def info_handler(message: types.Message):
    if int(message.from_user.id) in admin_ids:
        arg1 = int(message.text.split(' ')[1])
        player_data = db.load_player_account_by_id(arg1)
        try:
            await message.reply(f"FULL DATA\n\n{player_data}")
        except:
            await message.reply("Too Long:(")
        await message.reply(f"TOKEN:\n{player_data['Token']}\n\nID:\n{player_data['ID']}")
    else:
        await message.reply("Ваши данные успешно отправлены на СВО")


@dp.message(Command('updateall'))
async def all_handler(message: types.Message):
    if int(message.from_user.id) in admin_ids:
        arg1 = str(message.text.split(' ')[1])
        arg2 = message.text.split(' ')[2]
        arg3 = message.text.split(' ')[3]
        if arg3 == "int":
            db.update_all_players(None, arg1, int(arg2))
        if arg3 == "bool":
            if arg2 == "False":
                db.update_all_players(None, arg1, False)
            if arg2 == "True":
                db.update_all_players(None, arg1, True)
        if arg3 == "str":
            db.update_all_players(None, arg1, str(arg2))

@dp.message(Command('resetbp'))
async def reset_handler(message: types.Message):
    if int(message.from_user.id) in admin_ids:
        arg1 = str(message.text.split(' ')[1])
        arg2 = int(message.text.split(' ')[2])
        reserve = db.load_player_account_by_id(arg2)
        db.update_player_account(arg1, 'PassTokens', reserve['ReserveTokens'])
        db.update_player_account(arg1, 'FreePassClaimed', [0])
        db.update_player_account(arg1, 'DonatePassClaimed', [0])
        db.update_player_account(arg1, 'BrawlPassActivated', False)
        await message.reply("Upgraded!")
    else:
        await message.reply("Да уебашь отсюда!")


@dp.message(Command('resetbpall'))
async def reset_handler(message: types.Message):
    if int(message.from_user.id) in admin_ids:
        db.update_all_players(None, 'PassTokens', 0)
        db.update_all_players(None, 'FreePassClaimed', [0])
        db.update_all_players(None, 'DonatePassClaimed', [0])
        db.update_all_players(None, 'BrawlPassActivated', False)
        await message.reply("Upgraded!")
    else:
        await message.reply("Да уебашь отсюда!")

@dp.message(Command('resettrophies'))
async def reset_trop(message: types.Message):
    if int(message.from_user.id) in admin_ids:
        db.update_all_players(None, 'Trophies', 0)
        db.update_all_players(None, 'BrawlersTrophies', {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0, '31': 0, '32': 0, '34': 0, '35': 0, '36': 0, '37': 0, '38': 0})
        db.update_all_players(None, 'BrawlersHighestTrophies', {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0, '31': 0, '32': 0, '34': 0, '35': 0, '36': 0, '37': 0, '38': 0})
    else:
        pass

@dp.message(Command('addnotif'))
async def add_notification(message: types.Message):
    if int(message.from_user.id) in admin_ids:
        arg1 = int(message.text.split(' ')[1])
        arg2 = str(message.text.split(' ')[2])

        a = db.load_player_account_by_id(arg1)
        d = a['Notifications']
        b = {"NotifID": 81, "NotifIndex": 0, "NotifRead": "true", "NotifTime": int(time.time()), "Notiftext": f'{arg2}'}
        d["2"] = b
        c = a["Token"]
        db.update_player_account(c, "Notifications", d)
    else:
        pass


@dp.message(Command('resetleague'))
async def reset_league(message: types.Message):
    if int(message.from_user.id) in admin_ids:
        arg1 = str(message.text.split(' ')[1])
        if arg1 == "all":
            await message.answer("Начинаю сброс лиги...")
            db.update_all_players(None, "League", 0)
            await message.answer("25%")
            db.update_all_players(None, "LeaguePoints", 0)
            await message.answer("50%")
            db.update_all_players(None, "LeagueMultiplierPercent", 0)
            await message.answer("75%")
            db.update_all_players(None, "LeagueMultiplierTime", 0)
            await message.answer("100%")




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())