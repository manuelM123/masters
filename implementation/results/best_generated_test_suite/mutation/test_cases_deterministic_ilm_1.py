from cut import *

def test_case_0():
	cut = calorie_intake_calc(191.68,187.97,58,'M',0.22,'M')
	cut.height = 150.84
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 194.19
	cut.weight = 95.57
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(141.17,199.82,80,'M',0.01,'E')
	cut.height = 150.62
	cut.age = 53
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 81.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.amount_exercise = 'S'
	cut.height = 171.76
	result_determine_calorie_intake = cut.determine_calorie_intake()

