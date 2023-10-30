from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.76,217.91,56,'F',0.1,'L')
	cut.height = 158.16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 135.11
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(135.23,187.35,50,'N',0.03,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.17

def test_case_2():
	cut = calorie_intake_calc(85.84,188.0,58,'M',0.26,'M')

