from cut import *

def test_case_0():
	cut = calorie_intake_calc(132.52,214.27,79,'N',0.21,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 210.04
	cut.weight = 159.43
	cut.bodyfat = 0.12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 49
	cut.age = 71

def test_case_1():
	cut = calorie_intake_calc(65.7,209.26,75,'N',0.11,'M')
	cut.bodyfat = 0.13
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.21

def test_case_2():
	cut = calorie_intake_calc(170.49,165.13,77,'M',0.04,'V')
	cut.bodyfat = 0.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 151.18
	cut.weight = 204.42
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 16

