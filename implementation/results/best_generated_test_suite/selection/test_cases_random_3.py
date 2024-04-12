from cut import *

def test_case_0():
	cut = calorie_intake_calc(122.84,185.47,52,'M',0.19,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.23
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 79
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 145.95
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(171.45,184.82,59,'M',0.11,'L')
	cut.amount_exercise = 'V'
	cut.gender = 'M'
	cut.bodyfat = 0.21
	cut.bodyfat = 0.01
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 216.63
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.age = 63

def test_case_2():
	cut = calorie_intake_calc(200.09,163.9,28,'F',0.07,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 160.58
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.height = 205.0
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

