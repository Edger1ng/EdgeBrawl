import asyncio
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.types import CallbackQuery
import os
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "7353668722:AAGHWRS85ot6ms1nmvsoWSk2nAzLZGwoSy4"
bot = Bot(token=TOKEN)
dp = Dispatcher()

try:
    with open('tap.json', 'r') as f:
        data = json.load(f)
        maindb = data['main']
        alldb = data['alldb']
    with open('link.json', 'r') as a:
        dat = json.load(a)
        linkdb = dat['main']
except json.JSONDecodeError:
    print("Warning! JSONDecodeError!")
    maindb = {}
    alldb = {'all': 0}  # Initialize alldb to avoid potential key errors
    linkdb = {}

def save_data():
    with open('tap.json', 'w') as f:
        json.dump({'main': maindb, 'alldb': alldb}, f)
    with open('link.json', 'w') as a:
        json.dump({'main': linkdb}, a)

@dp.message(Command('start'))
async def start(message: types.Message):
    user_id = str(message.from_user.id)
    try:
        useee = maindb[user_id]['Coins']
        print(useee)
    except KeyError:
        maindb[user_id] = {"Coins": 0, "Level": 1}
        save_data()
        useee = maindb[user_id]['Coins']

    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Вывести коины", callback_data="out_coin"))
    
    allcoins = alldb['all']
    if allcoins == 0:
        kurs = 0
    else:
        kurs = 3200000 / allcoins
        
    gems = useee * kurs
    
    if int(gems) >= 0:
        await message.reply(f"Привет!\n\n1 Уровень Edge Tap окончен!\nПодробнее: https://t.me/edgetap/42\n\nТвои гемы для вывода: {gems}", reply_markup=builder.as_markup())
    else:
        await message.reply(f"Привет!\n\n1 Уровень Edge Tap окончен!\nПодробнее: https://t.me/edgetap/42\n\nУ тебя было настолько мало коинов, что ты не имеешь право на их вывод(кол-во гемов меньше 1)")

@dp.callback_query(F.data == 'out_coin')
async def out_coin(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    #builder.row(types.InlineKeyboardButton(text="Да, я согласен!", callback_data="out_coin2"))
    await callback.message.answer("ВАЖНО!!!\nИнструкция:\n\n1)Зайдите и нажмите /start в @edgeconnect_bot (Нужно дождаться до того момента, пока бот не ответит)\n2)Привяжите аккаунт (Опционально)\n\nЕсли вы сделали все, нажмите на кнопку")

@dp.callback_query(F.data == 'out_coin2')
async def out(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    try:
        gems_wallet = linkdb[user_id]['GemsWallet']
    except KeyError:
        linkdb[user_id] = {'GemsWallet': 0}
        gems_wallet = linkdb[user_id]['GemsWallet']
    
    allcoins = alldb['all']
    if allcoins == 0:
        kurs = 0
    else:
        kurs = 3200000 / allcoins
    
    gems = maindb[user_id]['Coins'] * kurs
    linkdb[user_id]['GemsWallet'] += gems
    maindb[user_id] = {"Coins": 0, "Level": 0}
    save_data()
    
    await callback.answer("Перенос выполнен.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
