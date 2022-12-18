import telebot
from bs4 import BeautifulSoup
import requests
from telebot import types

from methods import search_film, search_full, search_actors, search_pic

# 5617127293:AAFNjtGv6hQfj4ohxJV3sOQLAXr9gEJeqjg

search = 'https://www.rottentomatoes.com/search?search='

# bot
bot = telebot.TeleBot("5617127293:AAFNjtGv6hQfj4ohxJV3sOQLAXr9gEJeqjg")


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/search':
        bot.send_message(message.from_user.id, "Какой фильм ты ищешь?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /search')


def get_name(message):
    global film
    film = search_film(message.text)

    if not film or film[0][0] == 'er':
        bot.send_message(message.from_user.id, 'Такого фильма не существует, попробуйте еще раз')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Выбери нужный фильм')
        get_var_names(message)


def get_var_names(message):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура

    if len(film) < 5 and len(film) != 0:
        key1 = types.InlineKeyboardButton(text=film[0][0] + ' - ' + film[0][1], callback_data='1')
        keyboard.add(key1)
        question = 'Какой фильм?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    else:
        key1 = types.InlineKeyboardButton(text=film[0][0] + ' - ' + film[0][1], callback_data='1')
        keyboard.add(key1)
        key2 = types.InlineKeyboardButton(text=film[1][0] + ' - ' + film[1][1], callback_data='2')
        keyboard.add(key2)
        key3 = types.InlineKeyboardButton(text=film[2][0] + ' - ' + film[2][1], callback_data='3')
        keyboard.add(key3)
        key4 = types.InlineKeyboardButton(text=film[3][0] + ' - ' + film[3][1], callback_data='4')
        keyboard.add(key4)
        key5 = types.InlineKeyboardButton(text=film[4][0] + ' - ' + film[4][1], callback_data='5')
        keyboard.add(key5)
        question = 'Какой фильм?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


def get_prom(message):
    global parameters
    global actors
    global pictures
    parameters = search_full(cor_film)
    actors = search_actors(cor_film)
    pictures = search_pic(cor_film)

    keyboard2 = types.InlineKeyboardMarkup()  # наша клавиатура
    key1 = types.InlineKeyboardButton(text='Выборочная информация', callback_data='14')
    keyboard2.add(key1)
    key2 = types.InlineKeyboardButton(text='Полная информация', callback_data='15')
    keyboard2.add(key2)
    key3 = types.InlineKeyboardButton(text='Назад к выбору фильма', callback_data='16')
    keyboard2.add(key3)
    key4 = types.InlineKeyboardButton(text='Поиск нового фильма', callback_data='17')
    keyboard2.add(key4)
    question = 'Что ты хочешь узнать об этом фильме?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard2)


def get_param(message):
    keyboard2 = types.InlineKeyboardMarkup()  # наша клавиатура
    key1 = types.InlineKeyboardButton(text='Год, Жанр, Продолжительность', callback_data='6')
    keyboard2.add(key1)
    key2 = types.InlineKeyboardButton(text='Оценки', callback_data='7')
    keyboard2.add(key2)
    key4 = types.InlineKeyboardButton(text='Что говорят критики', callback_data='9')
    keyboard2.add(key4)
    key5 = types.InlineKeyboardButton(text='Режиссеры', callback_data='10')
    keyboard2.add(key5)
    key6 = types.InlineKeyboardButton(text='Постер', callback_data='11')
    keyboard2.add(key6)
    key7 = types.InlineKeyboardButton(text='Актеры', callback_data='12')
    keyboard2.add(key7)
    key8 = types.InlineKeyboardButton(text='Назад', callback_data='13')
    keyboard2.add(key8)
    question = 'Что конкретно ты хочешь узнать об этом фильме?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard2)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global cor_film
    if call.data == "1":
        cor_film = film[0][2]
        bot.send_message(call.message.chat.id, film[0][2])
        bot.register_next_step_handler(call.message, get_prom)
        bot.send_message(call.message.chat.id, 'Чтобы перейти в следующее меню напиши любое сообщение :)')
    elif call.data == "2":
        bot.send_message(call.message.chat.id, film[1][2])
        cor_film = film[1][2]
        bot.register_next_step_handler(call.message, get_prom)
        bot.send_message(call.message.chat.id, 'Чтобы перейти в следующее меню напиши любое сообщение :)')
    elif call.data == "3":
        bot.send_message(call.message.chat.id, film[2][2])
        cor_film = film[2][2]
        bot.register_next_step_handler(call.message, get_prom)
        bot.send_message(call.message.chat.id, 'Чтобы перейти в следующее меню напиши любое сообщение :)')
    elif call.data == "4":
        bot.send_message(call.message.chat.id, film[3][2])
        cor_film = film[3][2]
        bot.register_next_step_handler(call.message, get_prom)
        bot.send_message(call.message.chat.id, 'Чтобы перейти в следующее меню напиши любое сообщение :)')
    elif call.data == "5":
        bot.send_message(call.message.chat.id, film[4][2])
        cor_film = film[4][2]
        bot.register_next_step_handler(call.message, get_prom)
        bot.send_message(call.message.chat.id, 'Чтобы перейти в следующее меню напиши любое сообщение :)')
    elif call.data == "6":
        bot.send_message(call.message.chat.id, parameters[0])
    elif call.data == "7":
        if parameters[1] == 'Отсутствует информация' or parameters[2] == 'Отсутствует информация':
            bot.send_message(call.message.chat.id, 'Отсутствует информация об оценках')
        else:
            mid = (int(parameters[1]) + int(parameters[2])) / 2
            bot.send_message(call.message.chat.id, 'Пользовательская оценка: ' + parameters[1] + "\n"
                             + 'Оценка критиков: ' + parameters[2] + "\n" + 'Средняя оценка: ' + str(mid))
    elif call.data == "9":
        bot.send_message(call.message.chat.id, parameters[3])
    elif call.data == "10":
        bot.send_message(call.message.chat.id, parameters[4])
    elif call.data == "11":
        if pictures != 'Постер отсутствует':
            bot.send_photo(call.message.chat.id, pictures)
        else:
            bot.send_message(call.message.chat.id, pictures)
    elif call.data == "12":
        bot.send_message(call.message.chat.id, actors)
    elif call.data == "13":
        bot.register_next_step_handler(call.message, get_prom)
        bot.send_message(call.message.chat.id, 'Чтобы перейти в следующее меню напиши любое сообщение :)')
    elif call.data == "14":
        bot.register_next_step_handler(call.message, get_param)
        bot.send_message(call.message.chat.id, 'Чтобы перейти в следующее меню напиши любое сообщение :)')
    elif call.data == "15":
        if pictures != 'Постер отсутствует':
            bot.send_photo(call.message.chat.id, pictures)
        else:
            bot.send_message(call.message.chat.id, pictures)
        if parameters[1] == 'Отсутствует информация' or parameters[2] == 'Отсутствует информация':
            infoRate = 'Отсутствует информация об оценках' + "\n"
        else:
            mid = (int(parameters[1]) + int(parameters[2])) / 2
            infoRate = 'Пользовательская оценка: ' + parameters[1] + "\n" + 'Оценка критиков: ' \
                       + parameters[2] + "\n" + 'Средняя оценка: ' + str(mid) + "\n"

        bot.send_message(call.message.chat.id, parameters[0] + "\n" + infoRate + parameters[3]
                         + "\n" + 'Режиссеры: ' + parameters[4] + "\n"
                         + 'Актерский состав: ' + "\n" + actors)
    elif call.data == "16":
        bot.register_next_step_handler(call.message, get_var_names)
        bot.send_message(call.message.chat.id, 'Чтобы вернуться в предыдущее меню напиши любое сообщение :)')
    elif call.data == "17":
        bot.register_next_step_handler(call.message, get_name)
        bot.send_message(call.message.chat.id, 'Какой фильм ты ищешь?')


bot.polling()
