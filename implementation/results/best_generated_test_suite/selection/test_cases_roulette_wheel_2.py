from cut import *

def test_case_0():
	cut = calorie_intake_calc(81.68,150.27,49,'N',0.3,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.28
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(198.68,219.27,60,'N',0.2,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(162.61,200.44,52,'F',0.12,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.15

