from cut import *

def test_case_0():
	cut = calorie_intake_calc(210.63,194.44,15,'M',0.09,'E')

def test_case_1():
	cut = calorie_intake_calc(73.72,211.22,28,'M',0.04,'S')
	cut.age = 77
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 197.51
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.73
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 56

def test_case_2():
	cut = calorie_intake_calc(201.93,185.73,26,'F',0.08,'M')
	cut.gender = 'M'
	cut.height = 161.51
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.height = 162.94

def test_case_3():
	cut = calorie_intake_calc(183.98,216.26,69,'M',0.01,'S')
	cut.weight = 47.82
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(138.19,209.83,18,'F',0.27,'L')
	cut.age = 26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

