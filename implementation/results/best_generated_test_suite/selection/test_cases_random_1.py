from cut import *

def test_case_0():
	cut = calorie_intake_calc(69.36,160.36,38,'F',0.13,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(134.23,203.93,45,'N',0.22,'L')
	cut.height = 154.72

