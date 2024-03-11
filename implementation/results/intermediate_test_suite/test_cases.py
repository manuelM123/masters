from cut import *

def test_case_0():
	cut = calorie_intake_calc(87.59,154.68,60,'F',0.06,'E')
	cut.age = 49
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 133.35

def test_case_1():
	cut = calorie_intake_calc(81.7,220.58,45,'M',0.26,'L')
	cut.weight = 187.77
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'

