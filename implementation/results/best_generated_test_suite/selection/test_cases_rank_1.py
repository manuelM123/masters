from cut import *

def test_case_0():
	cut = calorie_intake_calc(60.17,174.52,39,'M',0.0,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(160.37,184.58,53,'M',0.21,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 21

