from cut import *

def test_case_0():
	cut = calorie_intake_calc(208.28,195.3,51,'F',0.05,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 210.84
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(190.46,152.56,18,'M',0.07,'S')
	cut.age = 65
	cut.gender = 'M'
	cut.height = 176.1
	cut.bodyfat = 0.03

