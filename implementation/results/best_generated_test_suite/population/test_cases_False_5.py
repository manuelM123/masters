from cut import *

def test_case_0():
	cut = calorie_intake_calc(108.58,207.27,12,'F',0.15,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.height = 163.29
	cut.height = 157.55
	cut.bodyfat = 0.23

def test_case_1():
	cut = calorie_intake_calc(178.97,163.56,65,'F',0.02,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.21
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 53.63
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(179.26,203.24,20,'N',0.14,'L')
	cut.bodyfat = 0.03
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 57
	cut.weight = 56.83
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.04
	cut.age = 59

