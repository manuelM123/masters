from cut import *

def test_case_0():
	cut = calorie_intake_calc(56.04,176.8,76,'F',0.02,'M')
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 41
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.14
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(54.68,180.65,19,'M',0.28,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(160.87,150.0,57,'N',0.14,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

