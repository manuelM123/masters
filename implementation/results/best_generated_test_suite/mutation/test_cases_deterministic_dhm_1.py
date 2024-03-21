from cut import *

def test_case_0():
	cut = calorie_intake_calc(145.35,183.07,52,'M',0.2,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 171.5

def test_case_1():
	cut = calorie_intake_calc(161.22,181.23,56,'N',0.07,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

