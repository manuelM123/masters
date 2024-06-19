from cut import *

def test_case_0():
	cut = calorie_intake_calc(74.31,176.94,26,'M',0.21,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(206.7,140.22,64,'F',0.26,'S')
	cut.weight = 138.65
	cut.weight = 156.21

