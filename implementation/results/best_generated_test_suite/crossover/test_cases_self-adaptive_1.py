from cut import *

def test_case_0():
	cut = calorie_intake_calc(115.56,190.88,54,'M',0.19,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(60.91,147.6,76,'N',0.04,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(56.33,156.96,15,'N',0.07,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 25

