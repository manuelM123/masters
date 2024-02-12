from cut import *

def test_case_0():
	cut = calorie_intake_calc(41.77,189.99,32,'M',0.27,'E')
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(199.1,213.07,77,'N',0.08,'N')
	cut.weight = 137.77
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

