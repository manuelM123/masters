from cut import *

def test_case_0():
	cut = calorie_intake_calc(103.56,209.75,53,'F',0.13,'E')
	cut.height = 202.66
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(136.33,152.47,26,'M',0.09,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 170.25
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 75
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'

