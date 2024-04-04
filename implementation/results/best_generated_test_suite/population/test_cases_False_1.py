from cut import *

def test_case_0():
	cut = calorie_intake_calc(59.09,140.37,70,'F',0.27,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'

def test_case_1():
	cut = calorie_intake_calc(135.95,196.78,25,'N',0.27,'E')

def test_case_2():
	cut = calorie_intake_calc(194.48,202.95,78,'N',0.13,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

