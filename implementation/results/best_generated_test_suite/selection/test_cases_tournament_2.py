from cut import *

def test_case_0():
	cut = calorie_intake_calc(144.45,190.31,66,'N',0.14,'S')

def test_case_1():
	cut = calorie_intake_calc(137.89,165.36,45,'F',0.03,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(107.29,182.46,45,'N',0.12,'E')
	cut.weight = 192.74
	cut.gender = 'N'
	cut.age = 40

