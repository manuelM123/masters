from cut import *

def test_case_0():
	cut = calorie_intake_calc(181.71,144.17,21,'F',0.09,'V')
	cut.height = 185.64
	cut.height = 176.45
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(82.67,216.57,74,'F',0.14,'E')
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.26
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(179.29,141.33,41,'M',0.08,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 149.53
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 194.28
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

