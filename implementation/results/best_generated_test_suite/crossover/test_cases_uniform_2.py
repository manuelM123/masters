from cut import *

def test_case_0():
	cut = calorie_intake_calc(116.34,186.58,42,'N',0.1,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(167.52,197.82,30,'M',0.16,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

