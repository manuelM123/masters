from cut import *

def test_case_0():
	cut = calorie_intake_calc(137.89,164.72,49,'M',0.1,'M')
	cut.height = 153.6
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(140.68,165.81,11,'F',0.06,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.height = 205.67
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 174.23
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 197.55

def test_case_2():
	cut = calorie_intake_calc(52.21,153.32,51,'F',0.29,'N')
	cut.age = 24
	cut.weight = 198.87
	cut.gender = 'M'
	cut.age = 26
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(152.94,181.99,49,'M',0.16,'V')
	result_tdee_calculation = cut.tdee_calculation()

