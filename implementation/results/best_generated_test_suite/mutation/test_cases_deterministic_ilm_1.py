from cut import *

def test_case_0():
	cut = calorie_intake_calc(133.75,220.93,45,'F',0.05,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 196.99
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(107.56,206.75,39,'F',0.01,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(95.75,190.05,61,'N',0.13,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

