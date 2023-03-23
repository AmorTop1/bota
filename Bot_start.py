import json
import telebot
from telebot import types

with open('settings.json') as _file:
    settings = json.load(_file)

token = settings.get('bot').get('token')
bot = telebot.TeleBot(token=token)
menu_message_id = None
calls = []


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Інструкція")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привіт! Я телеграм бот який вибере тобі мобільну гру. Нажми на кнопку.", reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text.startswith('Інструкція'))
def instruction(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_1 = types.KeyboardButton('Почати')
    markup.add(item_1)
    bot.send_message(message.chat.id, text="УВАГА!!!\nКоли ти нажмеш на любий жанр почекай 3 секунди і там будуть ігри, їх характеристики.\nТепер як розпроділити де гра а де її характеристики:\n[Назва гри]; [Розробник гри]; [Скільки поставили зірок цій грі]; [Скільки людей скачали цю гру]", reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text.startswith('Почати'))
def arrr(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_1 = types.KeyboardButton('Аркади')
    item_2 = types.KeyboardButton('Вікторини')
    item_3 = types.KeyboardButton('Головоломки')
    item_4 = types.KeyboardButton('Шутери')
    item_5 = types.KeyboardButton('Карткові')
    item_6 = types.KeyboardButton('Музика')
    item_7 = types.KeyboardButton('Перегони')
    item_8 = types.KeyboardButton('Пригодницкі')
    item_9 = types.KeyboardButton('Рольові')
    item_10 = types.KeyboardButton('Симулятори')
    item_11 = types.KeyboardButton('Словесні')
    item_12 = types.KeyboardButton('Спортивні')
    item_13 = types.KeyboardButton('Стратегіїчні')
    item_14 = types.KeyboardButton('Хоррор')
    markup.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11,
               item_12, item_13, item_14)
    bot.send_message(message.chat.id, text="Вибери категорію:", reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()
