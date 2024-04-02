from cut import *

def test_case_0():
	cut = calorie_intake_calc(140.67,197.62,13,'F',0.22,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(102.73,212.67,65,'F',0.14,'V')
	cut.amount_exercise = 'V'

def test_case_2():
	cut = calorie_intake_calc(144.35,175.01,74,'M',0.17,'M')
	cut.weight = 158.89
	cut.height = 181.42
	cut.amount_exercise = 'M'
	cut.gender = 'N'

