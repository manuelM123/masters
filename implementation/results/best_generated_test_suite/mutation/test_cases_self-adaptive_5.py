from cut import *

def test_case_0():
	cut = calorie_intake_calc(180.4,151.77,79,'N',0.09,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.2
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(153.83,190.42,60,'M',0.15,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

