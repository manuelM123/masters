from cut import *

def test_case_0():
	cut = calorie_intake_calc(204.64,144.76,12,'M',0.16,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 91.62

def test_case_1():
	cut = calorie_intake_calc(125.72,151.8,48,'M',0.04,'E')
	cut.age = 19
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 64.87
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

