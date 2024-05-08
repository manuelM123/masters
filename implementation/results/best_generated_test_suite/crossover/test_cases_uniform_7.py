from cut import *

def test_case_0():
	cut = calorie_intake_calc(64.93,204.75,62,'M',-0.26,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.gender = 'N'
	cut.age = 46
	cut.bodyfat = -0.18
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 52.8

def test_case_1():
	cut = calorie_intake_calc(205.43,150.86,37,'F',0.23,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.51
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 84

