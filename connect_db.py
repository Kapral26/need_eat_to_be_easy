# -*- coding: utf-8 -*-
import sqlite3 as sqlite
from os import path

class ConnectDB:
    __chk_usr = 'SELECT tg_login FROM users where tg_login = "{0}"'
    __insrt_new_usr = 'INSERT INTO users(tg_login)VALUES("{0}")'

    def __init__(self):
        self.proj_path = path.dirname(__file__)
        self.db_file = path.abspath(self.proj_path + "/db/food_and_dish_db.db")
        self.connect()

    def connect(self):
        self.conn = sqlite.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def chk_users(self, username):
        sql = self.__chk_usr.format(username)
        self.cursor.execute(self.__chk_usr.format(username))
        usr = self.cursor.fetchall()
        if usr == []:
            sql1 = self.__insrt_new_usr.format(username)
            self.cursor.execute(self.__insrt_new_usr.format(username))
            self.conn.commit()
        else:
            return True

if __name__ == '__main__':
    usr = 'kapral_26'
    ConnectDB().chk_users(usr)