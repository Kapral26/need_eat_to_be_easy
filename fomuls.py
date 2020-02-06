# -*- coding: utf-8 -*-


class NameClass:
	def __init__(self):
		pass

	def start_calc(self, sex, weight, hight, age, activity=None):
		if sex == 'm':
			formula_res = 9.99 * weight + 6.25 * hight - 4.92 * age + 5
		elif sex == 'w':
			formula_res = 9.99 * weight + 6.25 * hight - 4.92 * age - 161
		else:
			print("m or w")

		koef = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

		result = formula_res * koef[1]

		text = """
				Для похудения: {0}
				Для поддержания: {1}
				Для набора {2}
		""".format(
				round((result - result * 0.2), 0),
				result,
				round((result + result * 0.2), 0)
		)

		print(text)


if __name__ == '__main__':
	NameClass().start_calc('m', 81, 179, 26)
