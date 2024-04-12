from cut import *

def test_case_0():
	cut = calorie_intake_calc(110.86,165.01,42,'M',0.2,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 175.66
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 128.93
	cut.age = 63
	cut.bodyfat = 0.25
	cut.weight = 191.42

def test_case_1():
	cut = calorie_intake_calc(88.72,154.55,63,'F',0.01,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.bodyfat = 0.01
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(194.16,147.54,26,'F',0.16,'L')
	cut.height = 172.93
	cut.height = 174.09

