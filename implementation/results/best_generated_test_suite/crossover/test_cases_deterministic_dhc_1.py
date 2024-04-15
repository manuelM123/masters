from cut import *

def test_case_0():
	cut = calorie_intake_calc(115.56,190.88,54,'M',0.19,'L')
	cut.bodyfat = 0.03
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(105.8,150.64,42,'N',0.3,'N')
	cut.gender = 'M'
	cut.age = 28

