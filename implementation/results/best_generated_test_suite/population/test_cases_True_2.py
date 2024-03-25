from cut import *

def test_case_0():
	cut = calorie_intake_calc(47.61,205.34,13,'M',0.13,'E')
	cut.height = 150.96
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(77.99,199.82,65,'M',0.13,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.19
	cut.bodyfat = 0.11
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.02
	cut.gender = 'F'
	cut.weight = 61.95
	cut.age = 28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'

