from discord.ext import commands, tasks
from datetime import datetime
from calendar import weekday
from time import sleep
import discord
import asyncio
import random
import time
import os

print("\n+-+-+-+-+-+-+-+-+-+-+-+-+\n")
print("Start bot...")
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+\n")

def get_date():

    daylist = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    year = int(datetime.today().strftime('%Y'))
    month = int(datetime.today().strftime('%m'))
    day = int(datetime.today().strftime('%d'))
    hour = int(datetime.today().strftime('%H'))
    weekday_num = weekday(year, month, day)  # Получаем номер от 0 до 6 текущего дня недели!
    day = daylist[weekday_num]  # Выбираем из списка по номеру текстовый вариант дня! Для красоты прост так!

    # Понедельник
    if day == "Понедельник":
        if int(hour) < 1:
            return timer("Офин", "01")
        elif int(hour) < 2:
            return timer("Каранда, Кзарка", "02")
        elif int(hour) < 3:
            return timer("Нубэр", "03")
        elif int(hour) < 14:
            return timer("Кутум", "14")
        elif int(hour) < 16:
            return timer("Нубэр", "16")
        elif int(hour) < 18:
            return timer("Каранда", "18")
        elif int(hour) < 20:
            return timer("Кутум", "20")
        else:
            return timer("Перезапуск", "24")

    # Вторник
    if day == "Вторник":
        if int(hour) < 1:
            return timer("Нубэр, Каранда", "01")
        elif int(hour) < 2:
            return timer("Кзарка", "02")
        elif int(hour) < 3:
            return timer("Каранда", "03")
        elif int(hour) < 14:
            return timer("Каранда", "14")
        elif int(hour) < 16:
            return timer("Кзарка", "16")
        elif int(hour) < 18:
            return timer("Кутум", "18")
        elif int(hour) < 20:
            return timer("Каранда", "20")
        else:
            return timer("Перезапуск", "24")

    # Среда
    if day == "Среда":
        if int(hour) < 1:
            return timer("Квинт, Мурака", "01")
        elif int(hour) < 2:
            return timer("Кутум", "02")
        elif int(hour) < 3:
            return timer("Нубэр", "03")
        elif int(hour) < 16:
            return timer("Каранда", "16")
        elif int(hour) < 18:
            return timer("Нубэр", "18")
        elif int(hour) < 20:
            return timer("Кзарка, Офин", "20")
        else:
            return timer("Перезапуск", "24")

    # Четверг
    if day == "Четверг":
        if int(hour) < 1:
            timer("Велл", "01")
        elif int(hour) < 2:
            return timer("Каранда", "02")
        elif int(hour) < 3:
            return timer("Кутум", "03")
        elif int(hour) < 14:
            return timer("Нубэр", "14")
        elif int(hour) < 16:
            return timer("Кутум", "16")
        elif int(hour) < 18:
            return timer("Нубэр", "18")
        elif int(hour) < 20:
            return timer("Кзарка", "20")
        else:
            return timer("Перезапуск", "24")

    # Пятница
    if day == "Пятница":
        if int(hour) < 1:
            return timer("Камос", "01")
        elif int(hour) < 2:
            return timer("Нубэр", "02")
        elif int(hour) < 3:
            return timer("Кзарка", "03")
        elif int(hour) < 14:
            return timer("Каранда", "14")
        elif int(hour) < 16:
            return timer("Кутум", "16")
        elif int(hour) < 18:
            return timer("Нубэр", "18")
        elif int(hour) < 20:
            return timer("Кзарка", "20")
        else:
            return timer("Перезапуск", "24")

    # Суббота
    if day == "Суббота":
        if int(hour) < 1:
            return timer("Офин", "01")
        elif int(hour) < 2:
            return timer("Кзарка, Нубэр", "02")
        elif int(hour) < 3:
            return timer("Кутум", "03")
        elif int(hour) < 10:
            return timer("Кзарка", "10")
        elif int(hour) < 12:
            return timer("Нубэр", "12")
        elif int(hour) < 14:
            return timer("Кутум", "14")
        elif int(hour) < 16:
            return timer("Квинт, Мурака", "16")
        elif int(hour) < 18:
            return timer("Каранда", "18")
        elif int(hour) < 20:
            return timer("Кутум", "20")
        else:
            return timer("Перезапуск", "24")

    # Воскресенье
    if day == "Воскресенье":
        if int(hour) < 2:
            return timer("Камос", "02")
        elif int(hour) < 3:
            return timer("Кзарка", "03")
        elif int(hour) < 10:
            return timer("Каранда", "10")
        elif int(hour) < 12:
            return timer("Кутум", "12")
        elif int(hour) < 14:
            return timer("Камос", "14")
        elif int(hour) < 16:
            return timer("Кутум", "16")
        elif int(hour) < 18:
            return timer("Велл", "18")
        elif int(hour) < 20:
            return timer("Нубэр, Кзарка", "20")
        else:
            return timer("Перезапуск", "24")

def timer(boss_name, boss_hour):
    whathourisit = (datetime.today().strftime('%H')) #(%H:%M:%S.%f')[:-5]
    whatminisit = (datetime.today().strftime('%M'))
    whatsecisit = (datetime.today().strftime('%S'))
    whatmillisit = (datetime.today().strftime('%f')[:-5])
    whattimeisit = (whathourisit + ":" + whatminisit + ":" + whatsecisit + "." + whatmillisit)

    if whattimeisit == "00:00:00.5":
        print("Глобальный перезапуск, подожди 10 секунд!")
        sleep(9)
        get_date()

    boss_spawned = (str(boss_hour) + ":00:01.0")
    if whattimeisit == boss_spawned:
        print("Появился босс, а скрипт уходит на 10 секундный перезапуск!")
        sleep(9)
        get_date()

    boss_countH = (int(boss_hour)) - (int(whathourisit)+1)
    boss_countM = 59 - int(whatminisit)
    boss_countS = 59 - int(whatsecisit)
    boss_countMill = 9 - int(whatmillisit)
    bosscloser = (boss_name + " " + str(boss_countH) + ":" + str(boss_countM) + ":" + str(boss_countS) + ":" + str(boss_countMill))
    return bosscloser

PREFIX=("#")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')

async def status_task():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Black Desert Online"), status=discord.Status('dnd'))
    await asyncio.sleep(5)
    status_sign = 'idle'
    while True:
        
        os.system('cls||clear')
        rand_time = random.uniform(5, 6)
        if status_sign == 'online':
            status_sign = 'idle'
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=get_date()), status=discord.Status(status_sign))
        elif status_sign == 'idle':
            status_sign = 'online'
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=get_date()), status=discord.Status(status_sign))
        print('Bot working.\nStatus: ' + str(status_sign) + '\nSleep: ' + str(rand_time))
        await asyncio.sleep(rand_time)
  
@bot.event
async def on_ready():
    print("Bot is dnd... Start cycle task...\n")
    bot.loop.create_task(status_task())



bot.run('________BOT_TOKEN_HERE________') # < You can create own discord app and get token.