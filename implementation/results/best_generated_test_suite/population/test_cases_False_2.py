from cut import *

def test_case_0():
	cut = calorie_intake_calc(126.65,174.28,26,'N',0.02,'N')

def test_case_1():
	cut = calorie_intake_calc(137.57,172.77,69,'F',0.23,'E')
	cut.weight = 105.9
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

