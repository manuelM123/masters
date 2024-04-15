from cut import *

def test_case_0():
	cut = calorie_intake_calc(134.32,197.67,18,'M',0.23,'V')

def test_case_1():
	cut = calorie_intake_calc(111.89,152.85,65,'F',0.22,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 140.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(115.22,214.88,81,'M',0.05,'N')
	cut.weight = 72.2
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

