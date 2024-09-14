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

db = DB()
TOKEN = "6135498699:AAFU-L6h58t5j76mTZoeOgiidPGXoOhLdWU"
bot = Bot(token=TOKEN)
dp = Dispatcher()

try:
    with open('dbase.json', 'r') as f:
        data = json.load(f)
        maindb = data['main']
        alldb = data['alldb']
    with open('link.json', 'r') as f:
        dataa = json.load(f)
        linkdb = dataa['main']
except json.JSONDecodeError:
    print("Warning!JSONDecodeError!")
    maindb = {}
    alldb = {}


def save_data():
    with open('dbase.json', 'w') as f:
        json.dump({
            'main': maindb,
            'alldb': alldb
        }, f)


def update_check(coins, multiplier2, user_id):
    if multiplier2 == 2:
        if coins >= 250:
            maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 250
            maindb[user_id]['Multiplier'] = maindb[user_id]['Multiplier'] + 1
            save_data()
            return 20
        else:
            return 200
    if multiplier2 == 3:
        if coins >= 500:
            maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 500
            maindb[user_id]['Multiplier'] = maindb[user_id]['Multiplier'] + 1
            save_data()
            return 30
        else:
            return 300
    if multiplier2 == 4:
        if coins >= 1000:
            maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 1000
            maindb[user_id]['Multiplier'] = maindb[user_id]['Multiplier'] + 1
            save_data()
            return 40
        else:
            return 400
    if multiplier2 == 5:
        if coins >= 2000:
            maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 2000
            maindb[user_id]['Multiplier'] = maindb[user_id]['Multiplier'] + 1
            save_data()
            return 50
        else:
            return 500
    if multiplier2 == 6:
        if coins >= 4000:
            maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 4000
            maindb[user_id]['Multiplier'] = maindb[user_id]['Multiplier'] + 1
            save_data()
            return 60
        else:
            return 600
    if multiplier2 == 7:
        if coins >= 8000:
            maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 8000
            maindb[user_id]['Multiplier'] = maindb[user_id]['Multiplier'] + 1
            save_data()
            return 70
        else:
            return 700
    if multiplier2 == 8:
        if coins >= 9000:
            maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 9000
            maindb[user_id]['Multiplier'] = maindb[user_id]['Multiplier'] + 1
            save_data()
            return 80
        else:
            return 800
    if multiplier2 == 9:
        if coins >= 9500:
            maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 9500
            maindb[user_id]['Multiplier'] = maindb[user_id]['Multiplier'] + 1
            save_data()
            return 90
        else:
            return 900
    if multiplier2 == 10:
        if coins >= 10000:
            maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 10000
            maindb[user_id]['Multiplier'] = maindb[user_id]['Multiplier'] + 1
            save_data()
            return 100
        else:
            return 1000
    else:
        if coins >= 12500:
            maindb[user_id]['Coins'] = maindb[user_id]['Coins'] - 12500
            maindb[user_id]['Multiplier'] = maindb[user_id]['Multiplier'] + 1
            save_data()
            return multiplier2 * 10
        else:
            return multiplier2 * 100


def hours_verify(a):
    b = maindb[a]['HourMultipiler']
    c = maindb[a]['Coins']
    if b == 0:
        if c >= 3500:
            maindb[a]['HourMultipiler'] = 1
            maindb[a]['Coins'] -= 3500
            save_data()
            return True
        else:
            return False
    if b == 1:
        if c >= 7000:
            maindb[a]['HourMultipiler'] = 2
            maindb[a]['Coins'] -= 7000
            save_data()
            return True
        else:
            return False
    if b == 2:
        if c >= 14000:
            maindb[a]['HourMultipiler'] = 3
            maindb[a]['Coins'] -= 14000
            save_data()
            return True
        else:
            return False
    if b == 3:
        if c >= 28000:
            maindb[a]['HourMultipiler'] = 4
            maindb[a]['Coins'] -= 28000
            save_data()
            return True
        else:
            return False
    if b == 4:
        if c >= 56000:
            maindb[a]['HourMultipiler'] = 5
            maindb[a]['Coins'] -= 56000
            save_data()
            return True
        else:
            return False
    if b == 5:
        if c >= 112000:
            maindb[a]['HourMultipiler'] = 6
            maindb[a]['Coins'] -= 112000
            save_data()
            return True
        else:
            return False
    else:
        return 100


def autocoin_check(a):
    b = maindb[a]['AutoMultipiler']
    c = maindb[a]['Coins']
    if b == 0:
        if c >= 1000:
            maindb[a]['AutoMultipiler'] = 1
            maindb[a]['Coins'] -= 1000
            save_data()
            return True
        else:
            return False
    if b == 1:
        if c >= 2000:
            maindb[a]['AutoMultipiler'] = 2
            maindb[a]['Coins'] -= 2000
            save_data()
            return True
        else:
            return False
    if b == 2:
        if c >= 4000:
            maindb[a]['AutoMultipiler'] = 3
            maindb[a]['Coins'] -= 4000
            save_data()
            return True
        else:
            return False
    if b == 3:
        if c >= 8000:
            maindb[a]['AutoMultipiler'] = 4
            maindb[a]['Coins'] -= 8000
            save_data()
            return True
        else:
            return False
    if b == 4:
        if c >= 16000:
            maindb[a]['AutoMultipiler'] = 5
            maindb[a]['Coins'] -= 16000
            save_data()
            return True
        else:
            return False
    if b == 5:
        if c >= 32000:
            maindb[a]['AutoMultipiler'] = 6
            maindb[a]['Coins'] -= 32000
            save_data()
            return True
        else:
            return False
    if b == 6:
        if c >= 64000:
            maindb[a]['AutoMultipiler'] = 7
            maindb[a]['Coins'] -= 64000
            save_data()
            return True
        else:
            return False
    else:
        return 1



def account_verify(id, minitoken):
    try:
        pl = db.load_player_account_by_id(id)
    except:
        return 1
    tok = pl['Token']
    if tok[:4] == minitoken:
        return 0, tok
    else:
        return 2



@dp.message(Command('start'))
async def start_main(message: types.Message):
    user_id = str(message.from_user.id)
    try:
         useee = maindb[user_id]['Coins']
         print(useee)
    except:
        maindb[user_id] = {"Token": 0, "ID": 0, "Coins": 0, "Multiplier": 1, "Limit": 1000, "LatestClick": 0, "SponsorClaimed": [], "League": 1, "Type": 2, "HourMultipiler": 0, "AutoMultipiler": 0, "AutoTime": 0, "AutoProcess": False}
    save_data()

    if maindb[user_id]['ID'] == 0:
        await message.answer("Приветствуем в Edge Explore!\nЗарабатывай(кликай) монеты, и получай награды!\nВажно, перед началом советуем тебе привзять аккаунт!\n\nЧтобы начать, напиши /explore")


@dp.message(Command('explore'))
async def explore_main(message: types.Message):
    user_id = str(message.from_user.id)
    #if maindb[user_id]['Type'] == 0 or 2:
        #builder = InlineKeyboardBuilder()
        #builder.row(types.InlineKeyboardButton(text="Хочу вывести", callback_data="link_account"))
        #builder.row(types.InlineKeyboardButton(text="Начать новое приключение", callback_data="explore_round"))
        #await message.answer(f'Привет!\n2 раунд окончен и мы во всю готовимся к 3 раунду!\nЕсли хочешь можешь вывести твои коины в гемы а если хочешь продолжить - просто подожди пока появится кнопка продолжения:)', reply_markup=builder.as_markup())
    if maindb[user_id]['Type'] == 1:
        await message.answer(f'Ты выбрал покинуть проект.Жаль, но ты больше не сможешь ничего заработать.')
    if maindb[user_id]['Type'] == 0 or 4 or 2:
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text="Клик", callback_data="explore_click"))
        builder.row(types.InlineKeyboardButton(text="Увеличить стоимость клика", callback_data="explore_upgrade"))
        builder.row(types.InlineKeyboardButton(text="Отправить EDGE COIN", callback_data="send_coin"))
    #builder.row(types.InlineKeyboardButton(text="Привязать аккаунт", callback_data="link_account"))
        builder.row(types.InlineKeyboardButton(text="Депозит", callback_data="deposit_explore"))
        builder.row(types.InlineKeyboardButton(text="Автоклик", callback_data="auto_explore"))
        builder.row(types.InlineKeyboardButton(text="Квесты", callback_data="quests"))
        user_id = str(message.from_user.id)
        coins = maindb[user_id]['Coins']

        await message.answer(f'Edge Explore!\nЗдесь ты можешь кликать свои монетке\nМонетак: {coins}',
                                  reply_markup=builder.as_markup())


@dp.callback_query(F.data.lower() == 'quests')
async def quests(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    if linkdb[user_id]['LinkLvl'] >= 1:
        id = linkdb[user_id]['ID']
        player_data = db.load_player_account_by_id(id)
        if "gem1_quest" not in maindb[user_id]['Quests']:
            if player_data['Gems'] >= 950:
                builder = InlineKeyboardBuilder()
                builder.row(types.InlineKeyboardButton(text="Забрать награду", callback_data="gem1_claim"))
                await callback.message.answer("Получи 950 гемов на свой аккаунт\nСтатус: Выполнено\n\nНаграда: 2500 монет", reply_markup=builder.as_markup())
            else:
                await callback.message.answer("Получи 950 гемов на свой аккаунт\nСтатус: Не выполнено\n\nНаграда: 2500 монет")
        if "donate1_quest" not in maindb[user_id]['Quests']:
            if player_data['DonateLvl'] >= 1:
                builder = InlineKeyboardBuilder()
                builder.row(types.InlineKeyboardButton(text="Забрать награду", callback_data="donate1_claim"))
                await callback.message.answer("Получи донат в игре\nСтатус: Выполнено\n\nНаграда: 8000 токенов", reply_markup=builder.as_markup())
            else:
                await callback.message.answer("Получи донат в игре\nСтатус: Не Выполнено\n\nНаграда: 8000 токенов")
        if "click1_quest" not in maindb[user_id]['Quests']:
            if maindb[user_id]['Coins'] >= 20000:
                builder = InlineKeyboardBuilder()
                builder.row(types.InlineKeyboardButton(text="Забрать награду", callback_data="click1_quest"))
                await callback.message.answer("Набери 20000 коинов на баланс\nСтатус: Выполнено\n\nНаграда: 4000 токенов", reply_markup=builder.as_markup())
            else:
                callback.message.answer("Набери 20000 коинов на баланс\nСтатус: Не Выполнено\n\nНаграда: 4000 токенов")
        else:
            await callback.message.answer("Вуху!нету квестов для выполнения!\n\nСледи за новостями, а пока - можешь кликать в обычном темпе!")
    else:
        await callback.message.answer("Для начала нужно привязать свой аккаунт к Edge Connect!\n\nПерейди в @edgeconnect_bot и пройди верификацию!")

@dp.callback_query(F.data.lower() == 'link_account')
async def link_explore(callback: CallbackQuery):
    await callback.answer('Чтобы вернутся проиши /explore')
    await callback.message.answer('Привет!\nЭтот раздел рассказывает как привзять твой аккаунт EDGE COIN к аккаунту EDGE BRAWL')
    await callback.message.answer('Вот подробная инструкция:\nЗайди в Edge Brawl, найди входящие\nПерейди во вкладку личное\nЗапомни твой ID и первые 4 символа TOKEN')
    await callback.message.answer('Вот примеры как это работает:\nID: 48593050\nTOKEN: d94G49fcfJ483DGJFnj493\n\n/link 48593050 d94G')

@dp.message(Command('link'))
async def link_main(message: types.Message):
    user_id = str(message.from_user.id)
    args = message.text.split()
    id = int(args[1])
    minitoken = str(args[2])
    result = account_verify(id, minitoken)
    if result[0] == 0:
        maindb[user_id]['Token'] = str(result[1])
        maindb[user_id]['ID'] = id
        maindb[user_id]['Type'] = 1
        save_data()

        coins = maindb[user_id]['Coins']
        gems = coins * 0.250

        # Снимаем монеты
        maindb[user_id]['Coins'] -= coins
        save_data()  # Сохраняем обновленное значение монет

        pl_data = db.load_player_account(id, str(result[1]))
        gems2 = pl_data['Gems']
        gems2 += int(gems)

        # Обновляем значение гемов
        db.update_player_account(str(result[1]), 'Gems', gems2)

        await message.answer('Успешно!\nГемы отправлены на ваш аккаунт по курсу: 1 EDGE COIN = 0.125 GEMS')

    if result[0] == 1:
        await message.answer('Не удалось загрузить твой аккаунт:(\nСкорее всего, ты неправильно ввел ')



    await message.answer('')


@dp.callback_query(F.data.lower() == 'send_coin')
async def explore_send(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    coins = maindb[user_id]['Coins']
    await callback.message.answer(f'Ваши монетки: {coins}\n\nВаш ID: {user_id}\nУчтите что при отправке снимется 10% комисии\nЧтобы отправить напишите\n/send ID сумма\nПример: /send 1 1000')


@dp.message(Command('send'))
async def coin_send(message: types.Message):
    user_id = str(message.from_user.id)
    args = message.text.split()
    id = str(args[1])
    coiner = int(args[2])
    coiner2 = coiner / 10

    if maindb[user_id]['Coins'] - coiner >= 0:
        coiner3 = coiner - coiner2
        maindb[id]['Coins'] = maindb[id]['Coins'] + int(coiner3)
        maindb[user_id]['Coins'] -= coiner  # Исправлено здесь
        save_data()
        await message.reply('Отправлено!')
    else:
        await message.reply('Недостаточно коинов!')



@dp.callback_query(F.data.lower() == "explore_round")
async def explore_round(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    if maindb[user_id]['Type'] == 1:
        callback.answer('Недоступно')
    else:
        maindb[user_id]['Type'] = 2
        save_data()
        callback.message.answer('Готово, пропиши /explore')



@dp.callback_query(F.data.lower() == 'explore_upgrade')
async def explore_upgrade(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    coins = maindb[user_id]['Coins']
    multiplier = maindb[user_id]['Multiplier']
    multiplier2 = maindb[user_id]['Multiplier'] + 1
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text=f'Обновить до {multiplier2} уровня', callback_data="explore_update"))
    print("What")
    await callback.message.answer(f'Ваши монетки: {coins}\nВаш множитель: {multiplier}',
                                  reply_markup=builder.as_markup())
    await callback.message.delete()
    await callback.answer('Чтобы вернутся пропиши /explore')


@dp.callback_query(F.data.lower() == 'explore_click')
async def explore_click(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    coins = maindb[user_id]['Coins']
    if maindb[user_id]['Type'] == 2:
        if alldb['all'] <= 5000000:
            user_id = str(callback.from_user.id)
            allcoins = alldb['all']
            allcoins += maindb[user_id]['Multiplier']
            alldb['all'] = allcoins
            coins = maindb[user_id]['Coins']
            coins += maindb[user_id]['Multiplier']
            maindb[user_id]['Coins'] = coins  # Update the coins in the maindb
            save_data()
            await callback.answer(f'Твои коины: {coins}, Всего накликано: {allcoins}/5 000 000')
            print("maked")
        else:
            await callback.answer(f'Твои коины: {coins}, Ожидайте 3 стадию!')
    else:
        await callback.answer(f'Ты выбрал другой путь.Прощай.')



@dp.callback_query(F.data.lower() == 'explore_update')
async def explore_update(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    coins = maindb[user_id]['Coins']
    multiplier = maindb[user_id]['Multiplier']
    multiplier2 = maindb[user_id]['Multiplier'] + 1
    gamec = update_check(coins, multiplier2, user_id)
    gamec2 = multiplier2 * 10
    if gamec == 100:
        callback.answer(f'Вы прокачали множитель до {multiplier2} уровня!')
    else:
        if gamec == multiplier2 * 10:
            await callback.answer(f'Вы прокачали множитель до {multiplier2} уровня!')
        else:
            await callback.answer(f'Не хватает монет!')


@dp.callback_query(F.data.lower() == "auto_explore")
async def auto_explore(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    user_id = str(callback.from_user.id)
    x = maindb[user_id]['HourMultipiler']
    x1 = maindb[user_id]['HourMultipiler'] + 1
    y = maindb[user_id]['AutoMultipiler']
    y1 = maindb[user_id]['AutoMultipiler'] + 1
    z = maindb[user_id]['AutoTime']
    a = maindb[user_id]['AutoProcess']
    zz = 3600 * x
    zz = int(time.time()) - z
    zzz = 3600 * x
    zzzz = int(time.time())  - z
    zzzzz = zzzz * y
    print(zz)
    print(zzz)
    print(z)
    print(zzzz)
    if a == False:
        builder.row(types.InlineKeyboardButton(text=f'Начать майнинг', callback_data="autoexplore_start"))
    else:
        if zzzzz >= zzz:
            if x == 0:
                pass
                print("pass")
            else:
                builder.row(types.InlineKeyboardButton(text=f'Забрать монеты( {zzz}/{zzz} ) ', callback_data="autoexplore_claim"))
        else:
            if x == 0:
                pass
                print("pass")
            else:
                builder.row(types.InlineKeyboardButton(text=f'Забрать монеты {zzzzz}/{zzz}', callback_data="autoexplore_claim"))
    
    
    builder.row(types.InlineKeyboardButton(text=f'Прокачать до {x1} уровня(часы)', callback_data="autoexplore_hours"))
    builder.row(types.InlineKeyboardButton(text=f'Прокачать коин/сек до {y1} уровня', callback_data="autoexplore_coin"))
    await callback.message.answer("Auto Exploring - прокачай автоклик.\nУчти что ты можешь прокачать как и время майнинга\nТакже обрати внимание что максимальное время на сколько можно прокачать - 6 часов/7 кликов(сам уровень останется навсегда)", reply_markup=builder.as_markup())


@dp.callback_query(F.data.lower() == "autoexplore_start")
async def autoexplore_start(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    a = maindb[user_id]['AutoProcess']
    if a == True:
        await callback.answer("Ты уже запустил процесс майнинга!")
    else:
        z = maindb[user_id]['AutoTime']
        z = int(time.time())
        maindb[user_id]['AutoTime'] = z
        a = True
        maindb[user_id]['AutoProcess'] = a
        save_data()
        await callback.answer("Ты начал процесс майнинга!")

@dp.callback_query(F.data.lower() == "autoexplore_claim")
async def autoexplore_claim(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    if maindb[user_id]['AutoProcess'] == True:
        x = maindb[user_id]['HourMultipiler']
        x1 = maindb[user_id]['HourMultipiler'] + 1
        y = maindb[user_id]['AutoMultipiler']
        y1 = maindb[user_id]['AutoMultipiler'] + 1
        z = maindb[user_id]['AutoTime']
        a = maindb[user_id]['AutoProcess']
        zz = 3600 * x
        zz = int(time.time()) - z
        zzz = 3600 * x
        zzzz = int(time.time())  - z
        zzzzz = zzzz * y

        if zzzzz >= zzz:
            coin = maindb[user_id]['Coins'] + zzz
            maindb[user_id]['Coins'] = coin
            maindb[user_id]['AutoProcess'] = False
            maindb[user_id]['AutoTime'] = 0
            alldb['all'] = alldb['all'] + zzz
            save_data()
        else:
            coin = maindb[user_id]['Coins'] + zzzzz
            maindb[user_id]['Coins'] = coin
            maindb[user_id]['AutoProcess'] = False
            maindb[user_id]['AutoTime'] = 0
            alldb['all'] = alldb['all'] + zzzzz
            save_data()
        await callback.answer("Останавливаем процесс...", show_alert=True)
    else:
        await callback.answer("Возникла ошибка!", show_alert=True)


@dp.callback_query(F.data.lower() == "autoexplore_hours")
async def autoexplore_hours(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    result = hours_verify(user_id)
    if result == True:
        await callback.answer("Вы прокачали часы!", show_alert=True)
    if result == False:
        await callback.answer("Вам не хватает монет!", show_alert=True)
    else:
        await callback.answer("Достигнут лимит/Неизвестная ошибка", show_alert=True)


@dp.callback_query(F.data.lower() == "autoexplore_coin")
async def autoexplore_coin(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    result = autocoin_check(user_id)
    if result == True:
        await callback.answer("Вы прокачали клик!", show_alert=True)
    if result == False:
        await callback.answer("Вам не хватает монет!", show_alert=True)
    else:
        await callback.answer("Достигнут лимит/Неизвестная ошибка", show_alert=True)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())