from cut import *

def test_case_0():
	cut = calorie_intake_calc(198.65,174.47,29,'F',0.1,'L')
	cut.age = 48
	cut.weight = 160.28
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 151.88
	cut.gender = 'N'
	cut.age = 53
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(41.12,181.26,22,'F',0.22,'E')
	cut.age = 58
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 207.61
	cut.amount_exercise = 'N'

def test_case_2():
	cut = calorie_intake_calc(149.72,169.0,35,'M',0.23,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 44
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.02
	cut.bodyfat = 0.04
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

