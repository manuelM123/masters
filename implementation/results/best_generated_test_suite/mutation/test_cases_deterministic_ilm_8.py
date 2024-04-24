from cut import *

def test_case_0():
	cut = calorie_intake_calc(203.98,200.46,62,'F',0.23,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(171.6,201.08,14,'M',0.16,'M')
	cut.height = 149.58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 141.33
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'

