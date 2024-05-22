from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.48,156.24,35,'M',-0.48,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 50.0
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.66
	cut.weight = 38.82
	cut.height = 214.18

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(167.13,188.43,53,'F',-0.24,'L')
	cut.age = 35
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 165.29
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 174.15
	cut.weight = 39.3

def test_case_3():
	cut = calorie_intake_calc(197.63,188.28,52,'N',0.67,'E')
	cut.amount_exercise = 'V'
	cut.bodyfat = -0.48
	cut.weight = 43.94
	cut.height = 136.53

