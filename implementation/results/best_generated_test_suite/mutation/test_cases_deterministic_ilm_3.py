from cut import *

def test_case_0():
	cut = calorie_intake_calc(171.22,216.26,23,'F',0.26,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 59
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 14

def test_case_1():
	cut = calorie_intake_calc(88.84,148.26,57,'M',0.09,'V')
	cut.bodyfat = 0.0
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.weight = 142.0
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 178.25

