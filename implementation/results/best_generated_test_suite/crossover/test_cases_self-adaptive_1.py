from cut import *

def test_case_0():
	cut = calorie_intake_calc(113.25,162.83,21,'M',0.08,'L')
	cut.amount_exercise = 'V'
	cut.height = 143.75
	cut.height = 194.1
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 135.86
	cut.weight = 178.1
	cut.height = 209.36
	cut.height = 208.34
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.11

def test_case_1():
	cut = calorie_intake_calc(137.09,156.96,45,'N',0.14,'M')
	cut.gender = 'F'
	cut.gender = 'F'
	cut.height = 172.56
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 55

def test_case_2():
	cut = calorie_intake_calc(126.67,182.35,65,'M',0.16,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 76
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.23
	cut.height = 145.7
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(140.19,181.22,47,'F',0.26,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 143.87
	cut.bodyfat = 0.15
	cut.weight = 135.79

