from cut import *

def test_case_0():
	cut = calorie_intake_calc(77.78,213.34,17,'F',0.05,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 167.72

def test_case_1():
	cut = calorie_intake_calc(207.33,218.18,55,'F',0.0,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

