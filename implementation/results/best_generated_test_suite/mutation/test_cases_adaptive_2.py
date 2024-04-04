from cut import *

def test_case_0():
	cut = calorie_intake_calc(196.67,196.14,62,'F',0.1,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(105.56,186.71,76,'F',0.24,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

