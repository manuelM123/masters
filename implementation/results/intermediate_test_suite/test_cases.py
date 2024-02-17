from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.32,170.24,51,'F',0.09,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.09

def test_case_1():
	cut = calorie_intake_calc(41.13,213.91,57,'F',0.08,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 154.08

