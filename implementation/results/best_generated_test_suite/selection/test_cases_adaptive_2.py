from cut import *

def test_case_0():
	cut = calorie_intake_calc(42.8,185.37,25,'M',0.0,'V')

def test_case_1():
	cut = calorie_intake_calc(102.85,164.38,60,'M',0.19,'V')
	cut.height = 189.72
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(97.94,159.38,56,'N',0.08,'L')
	cut.age = 39
	cut.weight = 105.95
	cut.bodyfat = 0.18
	result_tdee_calculation = cut.tdee_calculation()

