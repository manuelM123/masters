from cut import *

def test_case_0():
	cut = calorie_intake_calc(65.36,149.39,71,'F',-0.17,'S')
	cut.bodyfat = 0.05
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 174.39
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.height = 216.11
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(204.96,221.43,79,'N',-0.24,'E')

def test_case_2():
	cut = calorie_intake_calc(113.03,198.47,78,'N',-0.36,'L')
	cut.age = 84
	cut.bodyfat = 0.63
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.height = 146.84
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

