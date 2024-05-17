from cut import *

def test_case_0():
	cut = calorie_intake_calc(194.87,170.54,38,'N',0.01,'V')
	cut.bodyfat = 0.0
	cut.height = 156.85
	cut.age = 19
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(151.15,142.23,55,'M',0.09,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

