from cut import *

def test_case_0():
	cut = calorie_intake_calc(85.41,199.68,74,'N',0.25,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(114.13,150.96,23,'F',0.23,'E')
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 155.53

def test_case_2():
	cut = calorie_intake_calc(202.88,187.44,72,'F',0.22,'M')
	cut.age = 39
	cut.weight = 210.3
	result_tdee_calculation = cut.tdee_calculation()

