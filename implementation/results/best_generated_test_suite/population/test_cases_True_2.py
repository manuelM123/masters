from cut import *

def test_case_0():
	cut = calorie_intake_calc(138.79,141.72,34,'F',0.23,'N')
	cut.bodyfat = 0.12

def test_case_1():
	cut = calorie_intake_calc(200.89,151.27,59,'F',0.25,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(109.49,156.13,34,'N',0.05,'V')

