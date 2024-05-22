from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 194.75
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.11
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.08
	cut.age = 69
	cut.age = 22

def test_case_1():
	cut = calorie_intake_calc(106.13,165.56,24,'N',0.69,'N')
	cut.amount_exercise = 'M'

def test_case_2():
	cut = calorie_intake_calc(71.87,178.85,36,'M',-0.33,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 162.77
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 171.14
	cut.age = 15
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19
	cut.age = 55

