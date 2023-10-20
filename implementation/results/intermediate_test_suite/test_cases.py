from cut import *

def test_case_0():
	cut = calorie_intake_calc(141.18,142.04,67,'F',0.01,'V')
	cut.height = 147.69

def test_case_1():
	cut = calorie_intake_calc(71.66,210.7,74,'M',0.24,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'

def test_case_2():
	cut = calorie_intake_calc(51.96,141.86,68,'F',0.19,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.01

def test_case_3():
	cut = calorie_intake_calc(40.92,159.12,15,'F',0.1,'E')
	cut.bodyfat = 0.08
	cut.gender = 'F'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

