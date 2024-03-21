from cut import *

def test_case_0():
	cut = calorie_intake_calc(143.76,144.15,51,'M',0.11,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.11
	cut.height = 188.15

def test_case_1():
	cut = calorie_intake_calc(204.97,218.57,33,'F',0.28,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

