from cut import *

def test_case_0():
	cut = calorie_intake_calc(196.21,215.67,42,'N',0.08,'V')

def test_case_1():
	cut = calorie_intake_calc(199.79,165.74,51,'F',0.28,'E')
	cut.age = 53
	cut.bodyfat = 0.17
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 139.1
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.14
	cut.height = 217.4

def test_case_2():
	cut = calorie_intake_calc(133.59,154.46,74,'F',0.15,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 77
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	cut.weight = 83.52

