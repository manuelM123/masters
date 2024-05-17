from cut import *

def test_case_0():
	cut = calorie_intake_calc(161.13,171.4,74,'F',-0.23,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.height = 159.01
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.67
	cut.bodyfat = 0.3

def test_case_1():
	cut = calorie_intake_calc(53.86,208.55,7,'N',0.34,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 55.37
	cut.bodyfat = -0.2
	cut.gender = 'M'
	cut.bodyfat = -0.24
	cut.weight = 76.86
	cut.height = 163.66

