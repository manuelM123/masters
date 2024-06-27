from cut import *

def test_case_0():
	cut = calorie_intake_calc(207.84,197.52,11,'F',-0.06,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'

def test_case_1():
	cut = calorie_intake_calc(54.21,161.49,14,'F',0.06,'S')
	cut.height = 204.73
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(95.24,214.41,82,'N',0.6,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 15
	cut.weight = 73.36
	cut.bodyfat = 0.17

