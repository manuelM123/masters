from cut import *

def test_case_0():
	cut = calorie_intake_calc(115.56,190.88,54,'M',0.19,'L')
	cut.weight = 171.41
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(111.89,152.85,65,'F',0.22,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 140.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

