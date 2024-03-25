from cut import *

def test_case_0():
	cut = calorie_intake_calc(40.67,146.43,18,'F',0.22,'V')
	cut.height = 165.61
	cut.height = 153.98
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 166.77
	cut.gender = 'N'
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.25
	cut.height = 207.45

def test_case_1():
	cut = calorie_intake_calc(162.93,174.45,51,'F',0.24,'E')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 164.88
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(59.24,181.9,23,'F',0.14,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 166.0
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 72
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.age = 36
	cut.gender = 'N'

