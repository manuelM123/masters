from cut import *

def test_case_0():
	cut = calorie_intake_calc(53.18,147.24,56,'N',0.04,'E')
	cut.bodyfat = 0.14

def test_case_1():
	cut = calorie_intake_calc(173.81,173.51,22,'F',0.03,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.01
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(131.52,164.32,61,'F',0.21,'S')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	cut.age = 11
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 63
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

