from cut import *

def test_case_0():
	cut = calorie_intake_calc(167.89,181.0,53,'M',0.06,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 41.8

def test_case_1():
	cut = calorie_intake_calc(69.08,206.26,14,'N',0.0,'E')
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'L'
	cut.weight = 138.48

