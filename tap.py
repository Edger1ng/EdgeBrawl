import asyncio
import json
# logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.types import CallbackQuery
import os
from aiogram.utils.keyboard import InlineKeyboardBuilder
from DataBase.DBManager import DB
import time

TOKEN="7353668722:AAGHWRS85ot6ms1nmvsoWSk2nAzLZGwoSy4"
bot = Bot(token=TOKEN)
db = DB()
dp = Dispatcher()

try:
    with open('tap.json', 'r') as f:
        data = json.load(f)
        maindb = data['main']
        alldb = data['alldb']
except json.JSONDecodeError:
    print("Warning!JSONDecodeError!")
    maindb = {}

def save_data():
    with open('tap.json', 'w') as f:
        json.dump({
            'main': maindb,
            'alldb': alldb
        }, f)

@dp.message(Command('start'))
async def start(message: types.Message):
    user_id = str(message.from_user.id)
    try:
        useee = maindb[user_id]['Coins']
        print(useee)
    except:
        maindb[user_id] = {"Coins": 0, "Level": 1}
        save_data()
    
    await message.reply("Edge Tap - проект, сделанный для Edge Brawl от команды @edgetap\n\nПочитать, что это такое: https://t.me/edgetap/6\n\nДля начала игры пропиши /tap")

@dp.message(Command('tap'))
async def tap_menu(message: types.Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.first_name)
    allcoins = alldb['all']
    kurs = 1600000 / allcoins
    kurs = kurs
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Тапнуть", callback_data="tap"))
    builder.row(types.InlineKeyboardButton(text="Прокачатся", callback_data="update"))
    builder.row(types.InlineKeyboardButton(text="Прокачать все", callback_data="update_all"))

    await message.reply(f"{user_name},\n\nВот главное меню Edge Tap.Ничего лишнего.\nТекущий курс: {kurs}", reply_markup=builder.as_markup())

@dp.callback_query(F.data.lower() == 'tap')
async def tap(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    coins = maindb[user_id]['Coins']
    user_id = str(callback.from_user.id)
    allcoins = alldb['all']
    allcoins += maindb[user_id]['Level']
    alldb['all'] = allcoins
    coins = maindb[user_id]['Coins']
    coins += maindb[user_id]['Level']
    maindb[user_id]['Coins'] = coins  # Update the coins in the maindb
    save_data()
    await callback.answer(f'Твои тапы: {coins}, Комьюнити: {allcoins}')
    print("maked")

@dp.callback_query(F.data.lower() == 'update')
async def update_tap(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    if maindb[user_id]['Coins'] >= 100:
        maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 100
        maindb[user_id]['Level'] = maindb[user_id]['Level'] + 1
        save_data()
        level = maindb[user_id]['Level']
        await callback.answer(f"Твой уровень теперь: {level}")
    else:
        await callback.answer("У тебя нет 100 монет.")

@dp.callback_query(F.data.lower() == 'update_all')
async def update_tap(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    if maindb[user_id]['Coins'] >= 100:
        mult = maindb[user_id]['Coins'] / 100
        mult = int(mult)
        mult2 = mult * 100
        maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - mult2
        maindb[user_id]['Level'] = maindb[user_id]['Level'] + mult
        save_data()
        level = maindb[user_id]['Level']
        await callback.answer(f"Твой уровень теперь: {level}")
    else:
        await callback.answer("У тебя нет 100 монет.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())