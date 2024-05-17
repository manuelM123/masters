from cut import *

def test_case_0():
	cut = calorie_intake_calc(64.43,173.36,15,'M',-0.22,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(171.13,151.48,20,'N',0.17,'E')
	cut.height = 188.94
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

