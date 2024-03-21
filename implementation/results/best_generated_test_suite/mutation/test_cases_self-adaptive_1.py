from cut import *

def test_case_0():
	cut = calorie_intake_calc(99.78,220.95,76,'F',0.15,'S')

def test_case_1():
	cut = calorie_intake_calc(61.97,209.68,62,'F',0.07,'E')
	cut.bodyfat = 0.25
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 193.35
	cut.gender = 'F'

