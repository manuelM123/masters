from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.42,179.3,69,'M',0.09,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(191.13,141.26,62,'M',0.28,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

