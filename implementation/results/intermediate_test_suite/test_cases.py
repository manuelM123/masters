from cut import *

def test_case_0():
	cut = calorie_intake_calc(158.45,170.94,50,'M',0.01,'S')
	cut.height = 184.25
	cut.bodyfat = 0.08
	cut.bodyfat = 0.26

def test_case_1():
	cut = calorie_intake_calc(155.26,181.52,76,'M',0.08,'L')
	cut.height = 210.61
	cut.height = 178.0
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

