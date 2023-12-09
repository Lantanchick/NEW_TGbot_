import time
import requests

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from aiogram.types.message import ContentType
from aiogram import Bot, Dispatcher, executor, types

from functional.functions import User

API_TOKEN = "6181834925:AAE-stlojDhCEE1ndAqualhgfiLlYAGgPp4"  # ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

KB1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb1_1 = KeyboardButton("/help")
kb1_2 = KeyboardButton("/🌠")
kb1_3 = KeyboardButton("/🌤")
kb1_4 = KeyboardButton("/reg")
KB1.add(kb1_1).insert(kb1_4)
KB1.add(kb1_3).insert(kb1_2)

KB2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb2_1 = KeyboardButton("/name-age")
kb2_2 = KeyboardButton("/password")
kb3_3 = KeyboardButton("/start")

user_text = None
user_log: User = None
users: list = []


def gen_photo_url(word: str) -> str:
    return "https://yandex.ru/images/search?text=" + word


def gen_weather_outer(city):
    return "https://yandex.ru/weather/ru-RU/" + city + "/details"


def gen_video_url(word):
    return "https://www.youtube.com/results?search_query=" + word


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="короткий текс от себя",
                           parse_mode="html",
                           reply_markup=KB1)
    await message.delete()

@dp.message_handler(commands=['reg'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="введите свое имя и возраст и нажмите команду /reg_user",
                           parse_mode="html",
                           reply_markup=KB2)
    await message.delete()

@dp.message_handler()
async def echo(message: types.Message):
    global user_text
    global user_log
    if message.text[0] != '/':
        user_text = message.text
    elif message.text == '/🌠':
        if user_text is None:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="вы еще ничего не ввели")
        else:
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo=gen_photo_url(user_text))
            await message.delete()
            user_text = None
    elif message.text == '/🌤':
        if user_text is None:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="вы еще ничего не ввели")
        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text=gen_weather_outer(user_text))
            await message.delete()
            user_text = None
    elif message.text == '/reg_user':
        if user_text is None:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="вы еще ничего не ввели")
        else:
            us = user_text.split()
            user_log = User(us[0], int(us[1]))
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Господин {us[0]} вы успешно зарегестрированы, "
                                        f"осталось ввести пароль и вызвать команду /password")
            user_text = None
    elif message.text == '/password':
        if user_text is None:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="вы еще ничего не ввели")
        else:
            user_log.save_user_password(user_text)
            await bot.send_message(chat_id=message.from_user.id,
                                   text="Пароль сохранен",
                                   reply_markup=KB1)
            user_text = None
            user_log.user_write()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
