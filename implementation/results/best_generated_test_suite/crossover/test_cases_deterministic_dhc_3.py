from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 194.75
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.11
	cut.amount_exercise = 'V'
	cut.bodyfat = -0.04
	cut.age = 69
	cut.age = 22

def test_case_1():
	cut = calorie_intake_calc(78.01,220.33,23,'N',0.38,'M')
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.54

def test_case_2():
	cut = calorie_intake_calc(183.99,179.4,72,'F',-0.1,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 89.22

def test_case_3():
	cut = calorie_intake_calc(109.57,196.3,59,'M',-0.5,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 135.51
	cut.gender = 'M'
	cut.bodyfat = 0.76
	cut.weight = 86.55
	cut.age = 20
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.02

