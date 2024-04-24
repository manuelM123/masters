from cut import *

def test_case_0():
	cut = calorie_intake_calc(206.21,156.85,29,'F',0.25,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.15
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'E'
	cut.weight = 77.3
	result_determine_calorie_intake = cut.determine_calorie_intake()

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
	cut = calorie_intake_calc(125.04,174.77,61,'N',0.24,'V')
	cut.age = 55
	cut.bodyfat = 0.28
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

