from cut import *

def test_case_0():
	cut = calorie_intake_calc(73.09,180.57,25,'N',0.19,'S')

def test_case_1():
	cut = calorie_intake_calc(67.96,157.64,68,'F',0.02,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 154.0

