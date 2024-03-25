from cut import *

def test_case_0():
	cut = calorie_intake_calc(46.71,211.73,56,'N',0.21,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.weight = 72.06
	cut.age = 57
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 185.28
	cut.age = 67
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(186.27,204.26,66,'N',0.26,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.12
	cut.height = 185.7
	cut.bodyfat = 0.3

