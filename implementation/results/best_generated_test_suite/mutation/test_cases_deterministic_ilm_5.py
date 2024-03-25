from cut import *

def test_case_0():
	cut = calorie_intake_calc(199.36,179.61,27,'M',0.13,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(74.22,148.15,62,'F',0.21,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.11
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

