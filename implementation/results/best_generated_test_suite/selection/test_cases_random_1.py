from cut import *

def test_case_0():
	cut = calorie_intake_calc(43.04,216.02,43,'M',0.25,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(201.59,176.53,33,'F',0.06,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

