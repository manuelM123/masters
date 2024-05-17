from cut import *

def test_case_0():
	cut = calorie_intake_calc(68.94,158.45,50,'F',0.13,'M')
	cut.height = 142.37
	cut.weight = 56.01

def test_case_1():
	cut = calorie_intake_calc(116.0,194.81,55,'M',0.42,'N')
	cut.age = 63
	cut.height = 214.45
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(135.72,191.09,31,'N',0.46,'N')
	cut.bodyfat = 0.3
	cut.amount_exercise = 'E'
	cut.weight = 84.46
	cut.bodyfat = 0.46
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.14
	cut.age = 35
	cut.weight = 69.06
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(65.4,149.24,69,'M',-0.31,'E')
	cut.height = 187.8
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 151.23
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 103.5
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 61

