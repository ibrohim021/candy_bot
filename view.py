# юда все функции отправляющие сообщения


from aiogram import types

from . import bot
import model
import commands


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Привет {message.from_user.first_name}\n'
                           f'На столе лежит 150 конфет, за один раз можно взять 28 штук\n'
                           f'первый ход обределяется жеребьевкой /lot')


async def end (message: types.Message):
    if model.winner == 1:
        await bot.send_message(message.from_user.id,
                            f'Ну и вали, жадина!')
    else:
        await bot.send_message(message.from_user.id,
                            f' До свидания, {message.from_user.first_name}!')


async def lotResult (message: types.Message):
    if model.lot == 1:
        await bot.send_message(message.from_user.id,
                        f' Первым ходит {message.from_user.first_name}')
    else:
        await bot.send_message(message.from_user.id,
                        f' Первым ходит МЕГАБОТ')
        await bot.send_message(message.from_user.id,
                        f'Ну что сразимся человечик  ')

async def showTotal (message: types.Message):
        await bot.send_message(message.from_user.id,
                        f' Осталось {model.count} конфет')

async def showBotSteep (message: types.Message):
        await bot.send_message(message.from_user.id,
                        f'МЕГА-Бот хапнул - {commands.steepBot} конфет')

async def showWinner (message: types.Message):
    if model.winner == 1:
        await bot.send_message(message.from_user.id,
                        f' Победитель {message.from_user.first_name}\n'
                        f' Хотите сыграть еще - нажмите /lot \n'
                        f' Уйти и не поделиться /finish ')
    else:
        await bot.send_message(message.from_user.id,
                        f' Победитель МЕГАБОТ \n'
                        f' Хотите продуть еще - нажмите /lot \n'
                        f' Уйти и остаться без сладкого /finish ')

async def wrongNumber (message: types.Message):
        await bot.send_message(message.from_user.id, 'Ах, ты хапуга')

async def wrongText (message: types.Message):
        await bot.send_message(message.from_user.id, 'Эх...')