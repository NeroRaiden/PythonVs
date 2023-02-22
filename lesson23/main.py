import aiogram
import random
import os
import logging
from decouple import config
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import math
API_TOKEN = '6268289456:AAEuF-rG5JBW1df0dNLfjNLEimvo9-7YRu0'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage
dp =Dispatcher (bot, storage = storage)

class GameState(StatesGroup):
    game = State()


def generate_math_example():
    first = random.randint(1,10)
    second = random.randint(1,10)
    operator = random.choice(['+','-','*','/'])
    return f'{first} {operator} {second}'

def generate_markup():
    true_math_example = generate_math_example()
    wrong_answers = [generate_math_example() for _ in range(3)]
    answers = (([true_math_example] + wrong_answers))
    random.shuffle (answers)

    markup = types.InlineKeyboardMarkup()
    markup.add(*[types.InlineKeyboardButton(ext = eval(answer),callback_data=answer) for answer in answers])
    return markup, true_math_example

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['start_game'],)
async def start_game(message: types.Message, state: FSMContext):
    await message.reply("Игра началась")
    await GameState.game.set()
    
    markup, true_math_example =generate_markup()
    await state.update_data(score=0, wrong=0, true_math_example=true_math_example)

    await message.reply(f'Скільки буде {true_math_example} ?' , reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data == 'start_game')
async def process_callback_game(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer('Ви відповіли на питання')
    data = await state.get_data()
    true_math_example = data.get('true_math_example')
    score = data.get('score')
    wrong = data.get('wrong')

    if callback_query.data == true_math_example:
        score +=1
        s_text = "Вірно!"
    else:
        wrong +=1
        s_text = 'Невірно!'

        markup, true_math_example = generate_markup()
        text =f's_text\n /stop_game для зупинки гри!\nВаш рахунок: {score}\n +''Наступне питання:'+f'Скільки буде {true_math_example}?'
        await callback_query.message.edit_text(text, reply_markup = markup)
        await state.update_data(score=score, true_math_example=true_math_example)

@dp.message_handler(commands=['stop_game'], state=GameState.game)
async def stop_game(message: types.Message, state: FSMContext):
    data = await state.get_data()
    score = data.get('score')
    wrong = data.get('wrong')
    
    if score > wrong:
        w_text = 'Вітаю! Ти переміг!'
        sticker_id = 'CAACAgIAAxkBAAIVdWP12GDawGJ47d5DNCpLKRT0BFteAALOGQACiRAQSoatMBZ4hfLALgQ'

    else:
        w_text = 'На жаль, ти програв.'
        sticker_id = 'CAACAgIAAxkBAAIVb2P12EXjGzKFEFqiXY7zmww3posuAAIKFwACMMHpSYyJhBXA0I3bLgQ'

    markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='Почати знову', callback_data = 'start_game'))
    await message.answer(f'{w_text}\nВаш рахунок: {score}\nКількість неправильних віжповідей: {wrong}, reply_markup=markup')
    await bot.send_sticker(message.chat.id, sticker_id)
    await state.finish()

@dp.message_handler(content_types=['sticker'])
async def sticker_id(message: types.Message):
    print(message.sticker.file_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)