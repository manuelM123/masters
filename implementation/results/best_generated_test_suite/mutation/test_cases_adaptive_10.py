from cut import *

def test_case_0():
	cut = calorie_intake_calc(187.03,163.56,65,'N',0.7,'E')

def test_case_1():
	cut = calorie_intake_calc(130.67,212.42,49,'M',0.0,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 51
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.6
	cut.bodyfat = 0.46

