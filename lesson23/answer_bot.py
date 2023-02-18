# Создать текстовые файлы с вариантами ответов на типичные фразы и вопросы:
# К примеру^
# Привет
# Как дела?
# Какая погода за окном?
# Как тебя зовут?
# Сколько тебе дней?
# Который час?
# и тд..
# далее написать функционала для бота
# который позволит при получении такого вопроса 
# от пользователя рандомно извлечь из 
# нужного файла ответ и в сообщении ответить пользователю.

# Вариативность должна быть не менее 5и разных ответов на один вопрос!

import json
import random

import logging
from aiogram import Bot, Dispatcher, executor, types
from decouple import config


API_TOKEN = config('TELE_API_KEY')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


inline_photo_button = types.InlineKeyboardMarkup()
inline_photo_button.add(types.InlineKeyboardButton("Котики", callback_data='cat'), 
            types.InlineKeyboardButton("Собачки", callback_data='dog'),
            types.InlineKeyboardButton("Попугаї", callback_data='parrot'))


folder_answers = 'lesson23/answers/'
init_file = json.load(open(folder_answers+'init.json', 'r', encoding='utf-8'))

def get_random_answer(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return random.choice(lines)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['photo'])
async def send_somephoto(message: types.Message):
    await message.reply("Обери варіанти фотографій👇", reply_markup=inline_photo_button)

@dp.callback_query_handler( lambda c: c.data in ['cat', 'dog', 'parrot'])
async def process_callback_kb1btn1(clq: types.CallbackQuery):
    path_photo = 'lesson23/data/photo/'+clq.data+'.txt'
    photo = get_random_answer(path_photo)
    await clq.message.answer_photo(photo=photo, caption='Ви обрали: '+clq.data, reply_markup=inline_photo_button)
    await clq.message.delete()

@dp.message_handler()
async def echo(message: types.Message):
    if message.text in init_file:
        path = folder_answers+init_file[message.text]
        answer = get_random_answer(path)
        await message.answer(answer)
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)