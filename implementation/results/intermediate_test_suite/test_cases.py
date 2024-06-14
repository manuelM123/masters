from cut import *

def test_case_0():
	cut = calorie_intake_calc(112.92,159.84,31,'F',0.72,'M')
	cut.weight = 119.42

def test_case_1():
	cut = calorie_intake_calc(39.58,180.42,31,'F',0.52,'L')
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

