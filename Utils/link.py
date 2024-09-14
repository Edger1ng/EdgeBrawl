import asyncio
import json
import random
# logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.types import CallbackQuery
import os
from aiogram.utils.keyboard import InlineKeyboardBuilder
from DataBase.DBManager import DB
import time

TOKEN="7379048322:AAF3oyhvv2_NmAJ_VBW_1FVTR8RZCPDYjnU"
bot = Bot(token=TOKEN)
db = DB()
dp = Dispatcher()

try:
    with open('link.json', 'r') as f:
        data = json.load(f)
        maindb = data['main']
except json.JSONDecodeError:
    print("Warning!JSONDecodeError!")
    maindb = {}

def save_data():
    with open('link.json', 'w') as f:
        json.dump({
            'main': maindb
        }, f)

@dp.message(Command('start'))
async def start_handler(message: types.Message):
    user_id = str(message.from_user.id)
    try:
        a = maindb[user_id]['Token']
        print(a)
    except:
        maindb[user_id] = {'Token': "0", 'ID': 0, 'LinkLvl': 0, 'TimeEveryday': 0, 'Transactions': {"xxx": {"Gems": 0, "TransID": "#TRxxx", "Comment": "Some, ok"}, "zzz": {"Gems": 0, "TransID": "#TRxxx", "Comment": "Some, ok"}}}
        save_data()
    builder = InlineKeyboardBuilder()
    if maindb[user_id]['LinkLvl'] == 0:
        builder.row(types.InlineKeyboardButton(text="Верифицировать аккаунт", callback_data="start_verificate"))
        await message.answer("Привет!\nЯ бот Edge Connect, и я позволяю управлять твоим аккаунтом в Edge Brawl!\nЯ могу:\n-Конвертировать твое золото в гемы\n-Переводить твои гемы другим игрокам\n-Удалять твой аккаунт\n-Переносить все твои игровые данные на другой аккаунт\n-А также давать тебе награды каждый день!\n\nОднако , тебе нужно верифицировать твой аккаунт.Не бойся, это не займет долго!", reply_markup=builder.as_markup())
    else:
        info2 = maindb[user_id]['ID']
        info = db.load_player_account_by_id(info2)
        name = info['Name']
        if maindb[user_id]['LinkLvl'] == 1:
            builder.row(types.InlineKeyboardButton(text="Повысить статус", callback_data="upgrade_verification"))
            builder.row(types.InlineKeyboardButton(text="Получить подарок", callback_data="everyday_gift"))
            builder.row(types.InlineKeyboardButton(text="Получить краткую сводку", callback_data="profile_info"))
            await message.answer(f"Панель управления аккаунтом {name}\nСтатус верификации: Базовый\n\nМногие функции ограничены.Повысьте свой статус верификации, и получите доступ к многим другим функциям.", reply_markup=builder.as_markup())
        if maindb[user_id]['LinkLvl'] == 2:
            builder.row(types.InlineKeyboardButton(text="Повысить статус", callback_data="upgrade_verification"))
            builder.row(types.InlineKeyboardButton(text="Получить подарок", callback_data="everyday_gift"))
            builder.row(types.InlineKeyboardButton(text="Получить краткую сводку", callback_data="profile_info"))
            builder.row(types.InlineKeyboardButton(text="Заморозить аккаунт", callback_data="freeze_account"))
            #builder.row(types.InlineKeyboardButton(text="Перевести гемы", callback_data="transfer_gems"))
            #builder.row(types.InlineKeyboardButton(text="Конвертировать монеты в гемы", callback_data="convert_coins"))
            #builder.row(types.InlineKeyboardButton(text="Сменить тему", callback_data="change_ground"))
            await message.answer(f"Панель управления аккаунтом {name}\nСтатус верификации: Расширенный\n\nНекоторые функции ограничены.Повысьте свой статус верификации, и получите доступ к некоторым другим функциям.", reply_markup=builder.as_markup())
        if maindb[user_id]['LinkLvl'] == 3:
            #builder.row(types.InlineKeyboardButton(text="Повысить статус", callback_data="upgrade_verification"))
            builder.row(types.InlineKeyboardButton(text="Получить подарок", callback_data="everyday_gift"))
            builder.row(types.InlineKeyboardButton(text="Получить краткую сводку", callback_data="profile_info"))
            builder.row(types.InlineKeyboardButton(text="Заморозить аккаунт", callback_data="freeze_account"))
            #builder.row(types.InlineKeyboardButton(text="Перевести гемы", callback_data="transfer_gems"))
            #builder.row(types.InlineKeyboardButton(text="Конвертировать монеты в гемы", callback_data="convert_coins"))
            builder.row(types.InlineKeyboardButton(text="Удалить аккаунт", callback_data="delete_account"))
            #builder.row(types.InlineKeyboardButton(text="Сменить тему", callback_data="change_ground"))
            await message.answer(f"Панель управления аккаунтом {name}\nСтатус верификации: Полный.\n\nНаслаждайся мощью полной верификации!\n\n/restore (NewID) - восстановление аккаунта", reply_markup=builder.as_markup())

@dp.callback_query(F.data.lower() == 'start_verificate' or 'upgrade_verification')
async def start_verificate(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    if maindb[user_id]['LinkLvl'] == 0:
        await callback.message.answer("Привет!Давай я помогу тебе верифицировать твой аккаунт!\n\nДля начала расскажу тебе что такое верификация")
        await callback.message.answer("Верификация - процесс подтверждения владения аккаунтом.В Edge Brawl на данный момент есть 3 уровня подтверждений")
        await callback.message.answer("1 уровень - самый базовый.Для получения данного уровня нужен твой Id и 4 первых символов TOKEN.Этот уровень дает мало чего.")
        await callback.message.answer("2 уровень дает тебе намного больше привелегий.Для данного уровня тебе нужен ID и 8 символов TOKEN")
        await callback.message.answer("3 уровень дает тебе все привелегии.Для него тебе нужно ID и 12 символов TOKEN")
        await callback.message.answer("Очень важно привязывать свой аккаунт сразу на полную привязку.Это дает всомое док-во того, что аккаунт ваш")
        await callback.message.answer("Примеры:\n/link 2483920 d7U1\n/link 2483920 d7U1IO14\n/link 2483920 d7U1IO14Pj0t")
    if maindb[user_id]['LinkLvl'] == 1:
        await callback.message.answer("Это очень хорошо что ты хочешь повысить свою верификацию.\nДумаю, всю важную информацию ты знаешь, однако напомню")
        await callback.message.answer("Примеры:\n/link 2483920 d7U1IO14 - Расширенная верификация\n/link 2483920 d7U1IO14Pj0t - Полная верификация")
    if maindb[user_id]['LinkLvl'] == 2:
        await callback.message.answer("Это очень хорошо что ты хочешь повысить свою верификацию.\nДумаю, всю важную информацию ты знаешь, однако напомню")
        await callback.message.answer("Примеры:\n/link 2483920 d7U1IO14Pj0t - Полная верификация")
    else:
        await callback.message.answer("Произошла неизвестная ошибка.Возможно, у вас уже максимальный уровень верификации.")

@dp.message(Command('link'))
async def verification_cmnd(message: types.Message):
    user_id = str(message.from_user.id)
    if maindb[user_id]['LinkLvl'] == 3:
        await message.answer("У тебя уже максимальный уровень верификации.")
    else:
        arg1 = int(message.text.split(' ')[1])
        arg2 = str(message.text.split(' ')[2])
        player_data = db.load_player_account_by_id(arg1)
        token = player_data['Token']
        isLinked = player_data['IsLinked']
        if player_data == None:
            await message.answer("Данного аккаунта не существует!Перепроверь данные!")
        if isLinked == True:
            await message.answer("Данный аккаунт уже привязан!\n\nЕсли вы считаете, что не привязывали аккаунт, сообщите в @edgefeedback_bot об этом как можно скорее!")
        else:
            if arg2 == token[:4]:
                if maindb[user_id]['LinkLvl'] == 0:
                    verif = 1
                    reward = random.choice([100, 150, 200])
                    gems = player_data['Gems'] + int(reward)
                    db.update_player_account(token, 'Gems', gems)
                    maindb[user_id]['LinkLvl'] = 1
                    maindb[user_id]['ID'] = player_data['ID']
                    maindb[user_id]['Token'] = player_data['Token']
                    save_data()
                    await message.answer(f"Поздравляю!Вы успешно верифицировали свой аккаунт!\n\nСостояние верификации: Базовый\n\nТакже был выдан приз в виде {reward} гемов!")
                else:
                    await message.answer("Ошибка!")
            if arg2 == token[:8]:
                if maindb[user_id]['LinkLvl'] == 1:
                    verif = 1
                    reward = random.choice([150, 200, 250, 300, 350])
                    gems = player_data['Gems'] + int(reward)
                    db.update_player_account(token, 'Gems', gems)
                    maindb[user_id]['LinkLvl'] = 2
                    maindb[user_id]['ID'] = player_data['ID']
                    maindb[user_id]['Token'] = player_data['Token']
                    save_data()
                    await message.answer(f"Поздравляю!Вы успешно верифицировали свой аккаунт!\n\nСостояние верификации: Расширенный\n\nТакже был выдан приз в виде {reward} гемов!")
                else:
                    await message.answer("Ошибка!")
            if arg2 == token[:12]:
                if maindb[user_id]['LinkLvl'] == 2:
                    verif = 1
                    reward = random.choice([200, 250, 300, 350, 400])
                    gems = player_data['Gems'] + int(reward)
                    db.update_player_account(token, 'Gems', gems)
                    maindb[user_id]['LinkLvl'] = 3
                    maindb[user_id]['ID'] = player_data['ID']
                    maindb[user_id]['Token'] = player_data['Token']
                    save_data()
                    await message.answer(f"Поздравляю!Вы успешно верифицировали свой аккаунт!\n\nСостояние верификации: Полный\n\nТакже был выдан приз в виде {reward} гемов!")
                else:
                    await message.answer("Ошибка!")
            else:
                if verif == 0:
                    await message.answer("Похоже, вы указываете не правильный код!")
                else:
                    pass

@dp.callback_query(F.data.lower() == 'everyday_gift')
async def everyday_gift(callback: CallbackQuery):
    reward = random.choice([1,2])
    user_id = str(callback.from_user.id)
    arg1 = maindb[user_id]['ID']
    player_data = db.load_player_account_by_id(arg1)
    token = player_data['Token']
    if int(time.time()) - maindb[user_id]['TimeEveryday'] <= 86400:
        await callback.message.answer("Еще не прошло 24 часа!")
    else:
        if reward == 1:
            reward = random.choice([100, 150, 200, 250, 300, 350, 400, 450, 500, 1000])
            tokens = player_data['PassTokens']
            tokens = tokens + reward
            db.update_player_account(token, 'PassTokens', tokens)
            maindb[user_id]['TimeEveryday'] = int(time.time())
            save_data()
            await callback.message.answer(f"Выдана ежедневная награда: {reward} очков прогресса Brawl Pass!")
        if reward == 2:
            reward = random.choice([5, 10, 15, 20, 25, 30, 35, 40])
            gems = player_data['Gems']
            gems = gems + reward
            maindb[user_id]['TimeEveryday'] = int(time.time())
            save_data()
            db.update_player_account(token, 'Gems', gems)
            await callback.message.answer(f"Выдана ежедневная награда: {reward} гемов")

@dp.callback_query(F.data.lower() == 'profile_info')
async def profile_info(callback: CallbackQuery):
    reward = random.choice([1,2])
    user_id = str(callback.from_user.id)
    arg1 = maindb[user_id]['ID']
    player_data = db.load_player_account_by_id(arg1)
    token = player_data['Token']
    trop = player_data['Trophies']
    gems = player_data['Gems']
    freezed = player_data['Maintenance']
    baned = player_data['Banned']
    await callback.message.answer(f"Данные:\n\nID: {arg1}\nКубки: {trop}\nГемы: {gems}\nЗаморожен: {freezed}\nЗаблокирован: {baned}")

@dp.callback_query(F.data.lower() == 'delete_account')
async def delete_account(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Да", callback_data="delete_ver"))
    await callback.message.answer("Внимание!\n\nВы собираетесь БЕЗВОЗВРАТНО удалить аккаунт.\nЕсли нажать ДА, то ваш аккаунт будет заблокирован, а его данные - сброшены.\n\nЕсли вы передумали, напишите /start", reply_markup=builder.as_markup())


@dp.callback_query(F.data.lower() == 'delete_ver')
async def delete(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    token = maindb[user_id]['Token']
    await callback.message.answer("Отвязываем аккаунт от аккаунта в Edge Brawl...")
    maindb[user_id]['ID'] = 0
    maindb[user_id]['Token'] = ' '
    save_data()
    await callback.message.answer("Ваш аккаунт Telegram больше не владеет аккаунтом Edge Brawl")
    await callback.message.answer("Удаляем аккаунт...")
    db.update_player_account(token, 'Ban', True)
    db.update_player_account(token, 'BanReason', 'Аккаунт был удален с помощью\n@edgeconect_bot')
    db.update_player_account(token, 'BanSupport', False)
    db.update_player_account(token, 'Gems', 0)
    db.update_player_account(token, 'Trophies', -999)
    db.update_player_account(token, 'Name', 'DELETED')
    await callback.message.answer("Ваш аккаунт был удален")

@dp.callback_query(F.data.lower() == 'freeze_account')
async def freeze_account(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    token = maindb[user_id]['Token']
    id = maindb[user_id]['ID']
    player_data = db.load_player_account_by_id(id)
    if player_data['MaintenanceType'] == 0:
        db.update_player_account(token, 'Maintenance', True)
        db.update_player_account(token, 'MaintenanceType', 2)
        await callback.message.answer("Аккаунт заморожен.Для разморозки нажмите ту же самую кнопку")
    if player_data['MaintenanceType'] == 2:
        db.update_player_account(token, 'Maintenance', False)
        db.update_player_account(token, 'MaintenanceType', 0)
    else:
        await callback.message.answer("Упс....Похоже, твоей заморозкой управляет поддержка Edge Brawl.")

@dp.callback_query(F.data.lower() == 'wallet')
async def wallet(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    token = maindb[user_id]['Token']
    id = maindb[user_id]['ID']
    player_data = db.load_player_account_by_id(id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Вывести Гемы"))

@dp.callback_query(F.data.lower() == 'convert_coins')
async def convert_coins(callback: CallbackQuery):
    user_id = str(callback.from_user.id)
    token = maindb[user_id]['Token']
    id = maindb[user_id]['ID']
    player_data = db.load_player_account_by_id(id)
    coins = player_data['Coins']

@dp.message(Command('restore'))
async def restore(message: types.Message):
    user_id = str(message.from_user.id)
    try:
        arg1 = int(message.text.split(' ')[1])
    except:
        await message.reply("Вы не указали ID!")
    if arg1 == maindb[user_id]['ID']:
        await message.reply("Нужно указывать новый ID аккаунта")
    else:
        try:
            old_acc = db.load_player_account_by_id(maindb[user_id]['ID'])
        except:
            await message.reply("У вас нет привязанного аккаунта!")
        try:
            new_acc = db.load_player_account_by_id(arg1)
        except:
            await message.reply("Невозможно загрузить аккаунт!")
        await message.reply("Получаем информацию о вашем старом аккаунте...")
        name = old_acc['Name']
        gems = old_acc['Gems']
        trophies = old_acc['Trophies']
        resources = old_acc['Resources']
        tokend = old_acc['TokenDoubler']
        high_tr = old_acc['HoghestTrophies']
        homebr = old_acc['HomeBrawler']
        profile_ico = old_acc['ProfileIcon']
        unlocked_br = old_acc['UnlockedBrawlers']
        br_trophies = old_acc['BrawlerTrophies']
        br_hightrophies = old_acc['BrawlerHighestTrophies']
        unlocked_skins = old_acc['UnlockedSkins']
        selected_skins = old_acc['SelectedSkins']
        brawlpass = old_acc['BrawlPassActivated']
        clubid = old_acc['ClubID']
        clubrole = old_acc['ClubRole']
        ban = old_acc['Ban']
        ban_reason = old_acc['BanReason']
        maintenance = old_acc['Maintenance']
        maintenance_type = old_acc['MaintenanceType']
        maintenance_text = old_acc['MaintenanceText']
        buyed = old_acc['Buyed']
        donate_lvl = old_acc['DonateLvl']
        pass_tokens = old_acc['PassTokens']
        free_claimed = old_acc['FreePassClaimed']
        donate_claimed = old_acc['DonatePassClaimed']
        await message.reply("Информация получена!")
        await message.reply("Начинаем восстановление...")

        id = new_acc['ID']
        token = new_acc['Token']
        token2 = old_acc['Token']

        db.update_player_account(token, 'Name', name)
        db.update_player_account(token, 'Gems', gems)
        db.update_player_account(token, 'Trophies', trophies)
        db.update_player_account(token, 'Resources', resources)
        db.update_player_account(token, 'TokenDoubler', tokend)
        db.update_player_account(token, 'HighestTrophies', high_tr)
        db.update_player_account(token, 'HomeBrawler', homebr)
        db.update_player_account(token, 'ProfileIcon', profile_ico)
        db.update_player_account(token, 'UnlockedBrawlers', unlocked_br)
        db.update_player_account(token, 'BrawlerTrophies', br_trophies)
        db.update_player_account(token, 'BrawlerHighestTrophies', br_hightrophies)
        db.update_player_account(token, 'UnlockedSkins', unlocked_skins)
        db.update_player_account(token, 'SelectedSkins', selected_skins)
        db.update_player_account(token, 'BrawlPassActivated', brawlpass)
        db.update_player_account(token, 'ClubID', clubid)
        db.update_player_account(token, 'ClubRole', clubrole)
        db.update_player_account(token, 'Ban', ban)
        db.update_player_account(token, 'BanReason', ban_reason)
        db.update_player_account(token, 'Maintenance', maintenance)
        db.update_player_account(token, 'MaintenanceType', maintenance_type)
        db.update_player_account(token, 'MaintenanceText', maintenance_text)
        db.update_player_account(token, 'Buyed', buyed)
        db.update_player_account(token, 'DonateLvl', donate_lvl)
        db.update_player_account(token, 'PassTokens', pass_tokens)
        db.update_player_account(token, 'FreePassClaimed', free_claimed)
        db.update_player_account(token, 'DonatePassClaimed', donate_claimed)

        maindb[user_id]['ID'] = id
        maindb[user_id]['Token'] = token
        save_data()

        db.update_player_account(token2, 'Ban', True)
        db.update_player_account(token2, 'BanReason', 'Аккаунт был удален с помощью\n@edgeconect_bot')
        db.update_player_account(token2, 'BanSupport', False)
        db.update_player_account(token2, 'Gems', 0)
        db.update_player_account(token2, 'Trophies', -999)
        db.update_player_account(token2, 'Name', 'DELETED')
        await message.reply("Восстановление аккаунта успешно завершено.Прошлый аккаунт был удален")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())