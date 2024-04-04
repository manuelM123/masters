from cut import *

def test_case_0():
	cut = calorie_intake_calc(124.08,156.91,22,'M',0.24,'E')

def test_case_1():
	cut = calorie_intake_calc(207.53,164.92,72,'F',0.19,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(134.28,203.24,65,'N',0.14,'N')

