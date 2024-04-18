from cut import *

def test_case_0():
	cut = calorie_intake_calc(96.38,147.44,26,'F',0.13,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 41.63
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(198.55,157.34,58,'F',0.12,'S')
	cut.height = 156.88

