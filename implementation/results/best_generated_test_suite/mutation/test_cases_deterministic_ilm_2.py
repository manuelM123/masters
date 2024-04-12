from cut import *

def test_case_0():
	cut = calorie_intake_calc(126.73,171.02,36,'M',0.06,'M')
	cut.height = 209.44
	cut.amount_exercise = 'M'
	cut.height = 204.11
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(81.28,160.89,64,'N',0.08,'L')
	cut.amount_exercise = 'V'

def test_case_2():
	cut = calorie_intake_calc(174.84,148.99,13,'M',0.08,'E')
	cut.weight = 135.13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 198.69
	cut.age = 45
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

