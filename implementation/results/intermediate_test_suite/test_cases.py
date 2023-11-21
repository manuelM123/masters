from cut import *

def test_case_0():
	cut = calorie_intake_calc(123.11,219.55,12,'N',0.03,'E')
	cut.height = 189.57
	cut.age = 66
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(151.61,187.58,30,'F',0.04,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(164.18,169.59,72,'F',0.15,'L')
	cut.weight = 194.17

def test_case_3():
	cut = calorie_intake_calc(144.13,177.75,61,'M',0.24,'E')
	cut.bodyfat = 0.21

