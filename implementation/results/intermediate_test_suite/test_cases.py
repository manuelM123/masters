from cut import *

def test_case_0():
	cut = calorie_intake_calc(68.65,151.57,54,'N',0.18,'S')

def test_case_1():
	cut = calorie_intake_calc(164.53,175.8,19,'N',0.11,'V')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 53
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

