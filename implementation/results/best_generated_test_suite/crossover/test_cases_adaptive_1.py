from cut import *

def test_case_0():
	cut = calorie_intake_calc(111.49,158.4,75,'N',0.24,'S')

def test_case_1():
	cut = calorie_intake_calc(110.14,204.12,71,'F',0.14,'V')
	result_tdee_calculation = cut.tdee_calculation()

