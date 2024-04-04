from cut import *

def test_case_0():
	cut = calorie_intake_calc(65.09,142.9,53,'F',0.11,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.17
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(198.19,212.6,27,'M',0.26,'M')
	cut.amount_exercise = 'E'
	cut.height = 205.5
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(153.67,200.53,52,'M',0.28,'E')
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

