from cut import *

def test_case_0():
	cut = calorie_intake_calc(170.12,153.49,18,'M',0.05,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(49.22,207.09,60,'F',0.15,'L')

