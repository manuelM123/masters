from cut import *

def test_case_0():
	cut = calorie_intake_calc(90.24,216.59,54,'F',0.25,'N')
	cut.age = 73
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(45.35,168.23,79,'M',0.23,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.height = 158.55

