from cut import *

def test_case_0():
	cut = calorie_intake_calc(72.74,216.03,43,'F',0.14,'S')
	cut.height = 213.05

def test_case_1():
	cut = calorie_intake_calc(65.48,181.76,67,'N',0.27,'S')
	cut.weight = 78.39
	cut.height = 200.81

def test_case_2():
	cut = calorie_intake_calc(152.65,151.26,28,'M',0.04,'V')
	cut.height = 146.0
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()

