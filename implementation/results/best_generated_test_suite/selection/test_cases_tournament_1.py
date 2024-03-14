from cut import *

def test_case_0():
	cut = calorie_intake_calc(82.7,141.83,78,'M',0.04,'S')

def test_case_1():
	cut = calorie_intake_calc(49.62,164.37,34,'F',0.19,'M')
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 48.91
	cut.bodyfat = 0.3

