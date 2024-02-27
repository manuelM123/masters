from cut import *

def test_case_0():
	cut = calorie_intake_calc(185.47,180.11,38,'F',0.16,'N')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(150.62,205.66,67,'F',0.26,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

