from cut import *

def test_case_0():
	cut = calorie_intake_calc(118.35,145.13,25,'F',0.23,'N')
	cut.weight = 123.12
	cut.height = 142.69
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.05

def test_case_1():
	cut = calorie_intake_calc(194.89,157.38,27,'M',0.19,'E')
	cut.weight = 121.72
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.gender = 'F'
	cut.age = 29
	cut.weight = 66.48
	cut.height = 158.53
	cut.height = 212.87

def test_case_2():
	cut = calorie_intake_calc(49.12,197.64,15,'N',0.28,'E')
	cut.bodyfat = 0.14
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 42.07
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.13
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 167.81
	cut.height = 196.1

def test_case_3():
	cut = calorie_intake_calc(40.28,199.22,68,'M',0.11,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 98.46
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

