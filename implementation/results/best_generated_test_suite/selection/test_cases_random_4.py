from cut import *

def test_case_0():
	cut = calorie_intake_calc(192.67,201.85,68,'N',0.13,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(178.7,156.33,49,'N',0.26,'L')
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.12
	cut.age = 78
	cut.bodyfat = 0.02
	cut.age = 55
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.17
	cut.weight = 206.07
	cut.weight = 87.93

def test_case_2():
	cut = calorie_intake_calc(202.92,160.48,67,'M',0.01,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 149.75
	cut.bodyfat = 0.0
	cut.gender = 'F'

def test_case_3():
	cut = calorie_intake_calc(177.91,201.29,22,'M',0.05,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.11
	cut.weight = 176.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.09

