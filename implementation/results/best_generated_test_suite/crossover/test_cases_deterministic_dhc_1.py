from cut import *

def test_case_0():
	cut = calorie_intake_calc(67.02,176.85,57,'M',0.14,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(107.41,157.82,51,'N',0.23,'S')
	result_tdee_calculation = cut.tdee_calculation()

