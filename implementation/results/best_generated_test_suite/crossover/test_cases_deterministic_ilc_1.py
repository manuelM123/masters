from cut import *

def test_case_0():
	cut = calorie_intake_calc(73.93,174.35,76,'F',0.73,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.height = 196.25

def test_case_1():
	cut = calorie_intake_calc(76.22,151.33,66,'M',0.37,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 161.46
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

