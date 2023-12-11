from cut import *

def test_case_0():
	cut = calorie_intake_calc(40.16,145.25,44,'N',0.03,'L')
	cut.weight = 80.61
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(54.62,209.82,26,'N',0.28,'E')
	cut.weight = 210.31
	cut.height = 190.45
	cut.bodyfat = 0.04
	cut.weight = 106.5

def test_case_2():
	cut = calorie_intake_calc(125.09,215.99,20,'N',0.24,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.07

