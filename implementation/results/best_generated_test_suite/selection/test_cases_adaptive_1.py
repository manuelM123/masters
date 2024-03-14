from cut import *

def test_case_0():
	cut = calorie_intake_calc(110.94,166.88,13,'M',0.01,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(57.57,192.8,25,'F',0.2,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 177.71
	result_tdee_calculation = cut.tdee_calculation()

