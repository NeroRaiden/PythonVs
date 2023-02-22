import os
import json
import random
import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ('6046567688:AAF4IhJ4YNuVgYOJ-By8lctJaA-wmJ0NHmY')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

IMAGE_DIR = 'Lesson22/photos/'

image_group ={
    'nature' : os.listdir(IMAGE_DIR+ 'nature'),
    'people' : os.listdir(IMAGE_DIR+ 'people'),
    'space' : os.listdir(IMAGE_DIR+ 'space')
}

word_options = {
    'image': ['картинка', 'картинки', 'картинкой', 'картинке', 'картинками', 'картинках', 'фото', 'фотография', 'фотографию'],
    'nature': ['природа','пейзаж','пейзажі','пейзажи','природу','природы','природи'],
    'people' : ['люди','людей','людьми','людям','людях','людям','людями'],
    'space' : ['космос','космосе','космоса','космосом','космосу']
}

def get_user_image_trigger(user_text):
    trigger1 = False
    trigger2 = False

    for word in user_text:
        if word in word_options['image']:
            trigger1 = True
    

    for key in list(word_options.keys())[1:]:
        if word in word_options[key]:
         trigger2 =True
        group = key
        break

    if trigger1 and trigger2:
        photo = random.choice(image_group[group])
        with open(IMAGE_DIR+group+'/'+photo, 'rb') as photo_file:
         return photo_file

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def send_somephoto(message: types.Message):
    user_text = message.text.lower().split()
    photo = get_user_image_trigger(user_text)
    if photo:
        await message.reply_photo(photo)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)