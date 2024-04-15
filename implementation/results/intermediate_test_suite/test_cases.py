from cut import *

def test_case_0():
	cut = calorie_intake_calc(158.58,145.15,79,'F',0.25,'L')
	cut.weight = 59.85
	cut.height = 149.83

def test_case_1():
	cut = calorie_intake_calc(77.21,195.98,74,'M',0.1,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'

