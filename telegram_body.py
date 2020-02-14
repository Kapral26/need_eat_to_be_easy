# -*- coding: utf-8 -*-
from os import path
import telebot
from connect_db import chk_users


class Telegram_bot:
    def __init__(self):
        self.get_bot_key()
        self.for_bot_test()

    def get_bot_key(self):
        key_file = path.join(path.dirname(__file__), "telegram_key.txt")
        with open(key_file) as file:
            self.token = file.read()
        print(self.token)

    def for_bot_test(self):

        bot = telebot.TeleBot(self.token)

        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            bot.reply_to(message, "Howdy, how are you doing?")

        @bot.message_handler(func=lambda message: True)
        def echo_all(message):
            ms_js = message.json['from']
            user = message, ms_js['username']
            if chk_users(user):
                print('user exist')
            else:
                print('user not exist')
            bot.reply_to(message, ms_js['username'])

        bot.polling()



if __name__ == "__main__":
    Telegram_bot()
