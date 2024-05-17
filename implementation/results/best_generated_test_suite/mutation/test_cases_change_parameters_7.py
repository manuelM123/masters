from cut import *

def test_case_0():
	cut = calorie_intake_calc(119.82,159.81,77,'N',0.38,'L')
	cut.gender = 'N'
	cut.age = 25
	cut.age = 15
	cut.gender = 'F'
	cut.height = 153.31
	cut.height = 142.1
	cut.age = 76

def test_case_1():
	cut = calorie_intake_calc(135.56,213.45,66,'F',0.08,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 74
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 159.08
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

