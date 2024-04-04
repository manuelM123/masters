from cut import *

def test_case_0():
	cut = calorie_intake_calc(146.98,212.88,10,'F',0.04,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(145.06,175.18,32,'N',0.21,'N')
	cut.bodyfat = 0.11

def test_case_2():
	cut = calorie_intake_calc(48.83,148.98,31,'F',0.07,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

