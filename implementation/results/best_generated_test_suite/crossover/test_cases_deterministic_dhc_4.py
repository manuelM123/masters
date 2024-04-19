from cut import *

def test_case_0():
	cut = calorie_intake_calc(77.09,169.97,33,'N',0.28,'V')
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(75.57,194.48,56,'N',0.02,'E')
	cut.weight = 182.56
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.05
	cut.weight = 144.74
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 165.35
	cut.height = 214.21
	cut.age = 60

