# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types
import model
import view
from . import bot
import random

async def start(message: types.Message):
    await view.greetings(message)

async def finish(message: types.Message):
    await view.end(message)

async def getLot(message: types.Message):
    model.lot = random.randint (1, 2)
    if model.lot == 1:
        await view.lotResult(message)
        model.count = 150
        await view.showTotal(message)
    else:
        await view.lotResult(message)
        model.count = 145
        await view.showTotal(message)


async def getNumber(message: types.Message):
    global number
    global steepBot
    number = message.text

    if number.isdigit() == True:
        if 0 < int(number) < 29:
            model.count = model.count - int (number)
            await view.showTotal(message)
            if model.count > 0:
                if model.count%model.turn == 0:
                    steepBot = random.randint (1, 28)
                    await view.showBotSteep(message)
                else:
                    steepBot = model.count%model.turn
                    await view.showBotSteep(message) 
                model.count = model.count - steepBot
                await view.showTotal(message)
                if model.count > 0:
                    model.winner = 1
                else:
                    model.winner = 2
                    await view.showWinner(message)
            else:
                model.winner = 1
                await view.showWinner(message)
        else:
            await view.wrongNumber(message)
    else:
        await bot.send_message(message.from_user.id, 'Эх ...')
    