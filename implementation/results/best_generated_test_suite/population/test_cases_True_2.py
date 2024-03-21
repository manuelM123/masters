from cut import *

def test_case_0():
	cut = calorie_intake_calc(73.03,162.44,49,'M',0.13,'N')
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(82.46,152.4,52,'F',0.04,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 157.07

def test_case_2():
	cut = calorie_intake_calc(152.66,207.89,80,'M',0.04,'N')

