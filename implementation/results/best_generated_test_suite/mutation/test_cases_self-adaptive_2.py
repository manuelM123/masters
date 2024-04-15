from cut import *

def test_case_0():
	cut = calorie_intake_calc(156.62,190.36,79,'N',0.25,'L')

def test_case_1():
	cut = calorie_intake_calc(137.89,165.36,45,'F',0.03,'M')
	cut.gender = 'M'
	cut.age = 28

def test_case_2():
	cut = calorie_intake_calc(107.29,182.46,45,'N',0.12,'E')
	cut.weight = 192.74
	cut.gender = 'N'
	cut.age = 40

def test_case_3():
	cut = calorie_intake_calc(96.52,181.82,42,'F',0.04,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.gender = 'M'
	cut.height = 164.45

