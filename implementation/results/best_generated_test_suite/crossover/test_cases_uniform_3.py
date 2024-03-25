from cut import *

def test_case_0():
	cut = calorie_intake_calc(133.02,192.18,61,'F',0.19,'S')
	cut.height = 177.37
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 187.16
	cut.age = 62
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(165.39,184.66,15,'M',0.07,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 21
	result_tdee_calculation = cut.tdee_calculation()

