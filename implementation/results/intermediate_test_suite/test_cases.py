from cut import *

def test_case_0():
	cut = calorie_intake_calc(203.71,159.76,58,'N',0.13,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 213.74
	cut.height = 188.36
	cut.age = 40
	cut.bodyfat = 0.44
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 208.6
	cut.age = 30
	cut.weight = 163.23
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.65

def test_case_1():
	cut = calorie_intake_calc(54.5,199.76,50,'M',0.51,'E')
	cut.age = 11

