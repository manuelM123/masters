from cut import *

def test_case_0():
	cut = calorie_intake_calc(66.14,151.35,50,'N',0.1,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 184.66
	cut.height = 147.39
	cut.height = 167.34

def test_case_1():
	cut = calorie_intake_calc(85.16,168.0,22,'F',0.13,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 66

