from cut import *

def test_case_0():
	cut = calorie_intake_calc(181.8,206.09,33,'M',0.04,'E')
	cut.weight = 160.19
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.amount_exercise = 'L'

def test_case_1():
	cut = calorie_intake_calc(194.51,207.99,80,'M',0.22,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

