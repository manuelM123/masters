from cut import *

def test_case_0():
	cut = calorie_intake_calc(63.93,184.62,76,'M',0.27,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 47

def test_case_1():
	cut = calorie_intake_calc(101.03,191.62,11,'M',0.21,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 49
	cut.height = 209.66

