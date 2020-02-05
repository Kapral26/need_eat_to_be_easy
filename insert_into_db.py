# -*- coding: utf-8 -*-
import sqlite3 as lite


class InserData:
	insert = "INSERT INTO food_and_dish(name, Proteins, Fats, Carbohydrates, Kcal) values({0});"

	def __init__(self):
		self.file = None #Файл откуда брвть данные для импорта
		db = None #Файл БД
		self.con = lite.connect(db)
		self.cur = self.con.cursor()

		self.work_with_file()

	def work_with_file(self):
		with open(self.file) as f:
			with open(self.create_script, "w") as inner:
				rows = f.readlines()[1:]
				for row in rows:
					l_row = row.replace("\n", "").replace(",", ".").split(";")
					name = '"{0}"'.format(l_row[0].strip())
					l_row.pop(0)
					l_row.insert(0, name)
					a = ','.join(l_row)
					sql = self.insert.format(a)
					try:
						self.cur.execute(sql)
						self.con.commit()
					except Exception as e:
						continue


if __name__ == '__main__':
	InserData()
