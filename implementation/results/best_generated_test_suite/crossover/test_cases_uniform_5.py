from cut import *

def test_case_0():
	cut = calorie_intake_calc(194.06,155.36,10,'F',0.28,'N')
	cut.weight = 179.97
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.44
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(102.59,145.79,38,'N',0.09,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 68
	cut.bodyfat = 0.02
	cut.height = 173.63
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()

