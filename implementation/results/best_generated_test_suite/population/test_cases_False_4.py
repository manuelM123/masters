from cut import *

def test_case_0():
	cut = calorie_intake_calc(195.79,218.26,74,'F',0.12,'E')
	cut.age = 37
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 43

def test_case_1():
	cut = calorie_intake_calc(184.97,202.9,52,'F',0.03,'M')
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(83.67,215.06,11,'N',0.2,'L')
	cut.weight = 58.61
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(128.72,204.6,50,'M',0.07,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 22
	cut.height = 155.14
	cut.weight = 107.66
	cut.weight = 63.02
	cut.weight = 141.88
	cut.height = 210.12
	cut.bodyfat = 0.27
	cut.bodyfat = 0.01
	cut.gender = 'N'

