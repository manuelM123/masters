from cut import *

def test_case_0():
	cut = calorie_intake_calc(57.86,193.34,57,'N',0.18,'S')
	cut.bodyfat = 0.23
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.2
	cut.age = 31
	cut.weight = 66.1
	cut.age = 42
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(86.21,158.37,50,'M',0.03,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.gender = 'N'
	cut.bodyfat = 0.3
	cut.age = 25
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()

