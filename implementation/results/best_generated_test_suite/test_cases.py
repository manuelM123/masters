from cut import *

def test_case_0():
	cut = calorie_intake_calc(194.29,144.55,33,'N',0.26,'V')
	cut.height = 194.47
	cut.weight = 52.45

def test_case_1():
	cut = calorie_intake_calc(180.39,187.52,47,'N',0.12,'E')

def test_case_2():
	cut = calorie_intake_calc(144.86,216.25,13,'M',0.22,'S')
	cut.weight = 55.38
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

