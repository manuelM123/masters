from cut import *

def test_case_0():
	cut = calorie_intake_calc(120.87,176.12,80,'F',0.24,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(86.67,180.88,38,'N',0.05,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(198.53,142.41,76,'F',0.15,'E')

