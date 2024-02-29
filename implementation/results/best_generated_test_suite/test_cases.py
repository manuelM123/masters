from cut import *

def test_case_0():
	cut = calorie_intake_calc(40.01,166.62,14,'F',0.2,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 144.05
	cut.amount_exercise = 'N'

def test_case_1():
	cut = calorie_intake_calc(75.86,165.11,77,'F',0.24,'V')
	cut.age = 11
	cut.amount_exercise = 'M'

def test_case_2():
	cut = calorie_intake_calc(104.16,179.91,56,'M',0.23,'V')
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(180.3,180.95,62,'N',0.11,'M')

def test_case_4():
	cut = calorie_intake_calc(115.61,145.15,14,'N',0.15,'M')

