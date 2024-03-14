from cut import *

def test_case_0():
	cut = calorie_intake_calc(122.45,202.12,49,'M',0.26,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 214.37
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'

def test_case_1():
	cut = calorie_intake_calc(74.52,156.11,77,'F',0.04,'V')
	result_tdee_calculation = cut.tdee_calculation()

