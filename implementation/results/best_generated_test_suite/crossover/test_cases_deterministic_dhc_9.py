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
	cut = calorie_intake_calc(157.14,184.87,45,'N',0.8,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.12
	cut.height = 183.79
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	cut.bodyfat = -0.48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.16

def test_case_2():
	cut = calorie_intake_calc(209.01,210.87,55,'M',0.61,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.bodyfat = -0.14
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 219.54
	cut.age = 59

