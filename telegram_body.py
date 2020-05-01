# -*- coding: utf-8 -*-
from os import path
import telebot
from connect_db import ConnectDB


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

		@bot.message_handler(commands=["start"])
		# @bot.message_handler(func=lambda message: True)
		def echo_all(message):
			ms_js = message.json["from"]
			user = ms_js["username"] if ms_js.get("username") else ms_js["first_name"]
			if ConnectDB().chk_users(user):
				msg = f"Снова привет мой старый друг - {user}"
			else:
				msg = f"Доброго дня {user}, надеюсь мы подружимся"
			bot.reply_to(message, msg)

		bot.polling()


if __name__ == "__main__":
	Telegram_bot()
