from cut import *

def test_case_0():
	cut = calorie_intake_calc(99.5,183.07,60,'F',0.11,'M')
	cut.height = 165.79
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.34

def test_case_1():
	cut = calorie_intake_calc(151.96,210.38,44,'M',0.13,'N')
	cut.height = 185.56
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

