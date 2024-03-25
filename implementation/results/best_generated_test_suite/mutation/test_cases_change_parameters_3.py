from cut import *

def test_case_0():
	cut = calorie_intake_calc(174.15,200.31,10,'F',0.26,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.15
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.12
	cut.amount_exercise = 'V'

def test_case_1():
	cut = calorie_intake_calc(98.36,182.72,18,'M',0.25,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.height = 155.43
	cut.bodyfat = 0.25
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 67.97
	cut.amount_exercise = 'S'

