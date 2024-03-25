from cut import *

def test_case_0():
	cut = calorie_intake_calc(113.05,197.79,60,'N',0.24,'N')
	cut.weight = 177.64
	cut.age = 72
	cut.age = 63
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 202.89
	cut.age = 61

def test_case_1():
	cut = calorie_intake_calc(208.28,198.7,10,'M',0.24,'M')
	cut.age = 31
	cut.weight = 205.99
	cut.bodyfat = 0.01
	cut.height = 180.64
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.age = 71

