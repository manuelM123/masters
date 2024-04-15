from cut import *

def test_case_0():
	cut = calorie_intake_calc(166.69,200.75,74,'N',0.22,'M')
	cut.weight = 131.69
	cut.height = 149.83

def test_case_1():
	cut = calorie_intake_calc(160.37,184.58,53,'M',0.21,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

