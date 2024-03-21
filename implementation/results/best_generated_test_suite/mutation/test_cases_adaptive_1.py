from cut import *

def test_case_0():
	cut = calorie_intake_calc(73.25,219.53,43,'N',0.06,'L')
	cut.bodyfat = 0.19
	cut.age = 78

def test_case_1():
	cut = calorie_intake_calc(175.42,149.27,18,'F',0.19,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.19
	cut.height = 158.02

def test_case_2():
	cut = calorie_intake_calc(163.39,199.31,56,'F',0.06,'N')

