from cut import *

def test_case_0():
	cut = calorie_intake_calc(204.29,186.21,23,'N',0.22,'L')

def test_case_1():
	cut = calorie_intake_calc(160.37,184.58,53,'M',0.21,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 21

