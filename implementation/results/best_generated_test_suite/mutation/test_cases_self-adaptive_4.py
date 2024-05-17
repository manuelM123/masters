from cut import *

def test_case_0():
	cut = calorie_intake_calc(90.3,140.17,38,'N',-0.39,'L')

def test_case_1():
	cut = calorie_intake_calc(69.8,147.4,28,'F',-0.38,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 183.14
	cut.gender = 'M'
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()

