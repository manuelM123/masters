from cut import *

def test_case_0():
	cut = calorie_intake_calc(196.78,192.96,10,'F',0.07,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.weight = 128.25

def test_case_1():
	cut = calorie_intake_calc(90.03,202.37,80,'N',0.05,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

