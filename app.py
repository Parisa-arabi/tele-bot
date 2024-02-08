import os
from telebot import *
import telebot
from PyMultiDictionary import MultiDictionary
from credentials import *
from Token import *

dictionary = MultiDictionary()

# BOT_TOKEN = "6701853868:AAF2XERaXsNIlhyRTEmZU85bBqSDoedmAQ8"

bot = telebot.TeleBot(BOT_TOKEN)


def generate_menu():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttons = [types.KeyboardButton("meaning"), types.KeyboardButton("synonym")]
    markup.add(*buttons)
    return markup


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hi there, what word are you looking for?")
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=generate_menu())


@bot.message_handler(func=lambda message: True)
def process_options(message):
    option = message.text
    if option == "meaning":
        bot.send_message(message.chat.id, "write down your word: ", reply_markup=None)
        bot.register_next_step_handler(message, process_meaning)
    elif option == "synonym":
        bot.send_message(message.chat.id, "write down your word: ")
        bot.register_next_step_handler(message, process_synonym)


def process_synonym(message):
    bot.reply_to(message, "This is your synonym " + "\n" + get_syn(message.text))

def process_meaning(message):
    bot.reply_to(message, "This is your meaning " + "\n" + get_mean(message.text))


bot.polling()