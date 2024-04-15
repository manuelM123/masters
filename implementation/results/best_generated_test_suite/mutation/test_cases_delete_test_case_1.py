from cut import *

def test_case_0():
	cut = calorie_intake_calc(70.66,165.51,12,'M',0.26,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(148.88,177.85,10,'F',0.26,'S')
	cut.bodyfat = 0.13
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.26
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

