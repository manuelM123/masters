from cut import *

def test_case_0():
	cut = calorie_intake_calc(59.38,219.58,35,'F',0.03,'E')
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 58
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 203.91
	cut.gender = 'F'
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(158.35,193.74,80,'F',0.19,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

