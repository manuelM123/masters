from cut import *

def test_case_0():
	cut = calorie_intake_calc(88.24,212.11,60,'M',0.08,'E')
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	cut.weight = 56.2
	cut.gender = 'M'
	cut.weight = 195.96
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(135.22,212.38,76,'N',0.25,'S')
	cut.bodyfat = 0.24

