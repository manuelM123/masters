from cut import *

def test_case_0():
	cut = calorie_intake_calc(194.49,161.9,72,'F',0.13,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 98.11
	cut.weight = 57.04
	cut.height = 218.27
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 210.4
	cut.height = 191.64
	cut.gender = 'N'
	cut.age = 14

def test_case_1():
	cut = calorie_intake_calc(175.07,143.62,73,'N',0.13,'L')
	cut.amount_exercise = 'L'

