# -*- coding: utf-8 -*-
import sqlite3 as lite
from os import path


class InserData:
	insert = "INSERT INTO food_and_dish(name, proteins, fats, carbohydrates, kcal) values({0});"

	def __init__(self):
		self.project_dir = path.dirname(__file__)
		self.file = path.join(self.project_dir, "table_to_next_processing")
		db = path.join(self.project_dir, "food_and_dish_db.db")
		self.con = lite.connect(db)
		self.cur = self.con.cursor()

		self.work_with_file()

	def work_with_file(self):
		with open(self.file, encoding='utf8') as f:
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
