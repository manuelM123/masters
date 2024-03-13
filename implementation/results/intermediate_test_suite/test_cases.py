from cut import *

def test_case_0():
	cut = calorie_intake_calc(182.68,178.98,58,'F',0.15,'M')
	cut.bodyfat = 0.12
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(209.66,149.23,20,'F',0.25,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

