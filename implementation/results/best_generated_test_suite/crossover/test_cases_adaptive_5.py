from cut import *

def test_case_0():
	cut = calorie_intake_calc(120.32,200.71,55,'M',-0.12,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 16
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.24

def test_case_1():
	cut = calorie_intake_calc(199.17,188.0,17,'F',0.09,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

