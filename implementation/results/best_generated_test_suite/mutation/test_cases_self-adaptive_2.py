from cut import *

def test_case_0():
	cut = calorie_intake_calc(212.86,158.79,36,'N',0.56,'L')

def test_case_1():
	cut = calorie_intake_calc(134.43,196.97,62,'M',0.28,'E')
	cut.age = 13
	cut.height = 207.09
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 195.76
	cut.age = 75
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.33
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.66

