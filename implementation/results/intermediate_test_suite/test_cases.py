from cut import *

def test_case_0():
	cut = calorie_intake_calc(203.52,207.51,23,'M',0.23,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(182.52,150.84,53,'F',0.01,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(66.76,181.71,23,'M',0.26,'V')
	cut.weight = 44.53
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

