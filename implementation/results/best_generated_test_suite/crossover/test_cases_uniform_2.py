from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.79,180.81,43,'N',0.25,'E')
	cut.age = 33
	cut.bodyfat = 0.29
	cut.bodyfat = 0.26

def test_case_1():
	cut = calorie_intake_calc(202.98,141.1,53,'M',0.08,'S')
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

