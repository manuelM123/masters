from cut import *

def test_case_0():
	cut = calorie_intake_calc(134.32,197.67,18,'M',0.23,'V')

def test_case_1():
	cut = calorie_intake_calc(125.64,213.25,13,'F',0.1,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 102.41
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'

