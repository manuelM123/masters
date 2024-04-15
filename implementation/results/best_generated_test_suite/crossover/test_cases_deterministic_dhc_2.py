from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.45,171.11,43,'F',0.02,'S')
	cut.weight = 131.69
	cut.height = 149.83

def test_case_1():
	cut = calorie_intake_calc(110.85,189.53,52,'F',0.14,'E')
	cut.weight = 71.58
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.08
	result_tdee_calculation = cut.tdee_calculation()

