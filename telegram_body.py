# -*- coding: utf-8 -*-
from os import path


class Telegram_bot:
    def __init__(self):
        self.get_bot_key()

    def get_bot_key(self):
        key_file = path.join(path.dirname(__file__), "telegram_key.txt")
        with open(key_file) as file:
            self.key = file.read()
        print(self.key)

if __name__ == "__main__":
    Telegram_bot()