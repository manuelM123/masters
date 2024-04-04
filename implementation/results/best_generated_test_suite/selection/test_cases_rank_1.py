from cut import *

def test_case_0():
	cut = calorie_intake_calc(141.0,216.51,75,'M',0.2,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(134.17,152.04,38,'M',0.01,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()

