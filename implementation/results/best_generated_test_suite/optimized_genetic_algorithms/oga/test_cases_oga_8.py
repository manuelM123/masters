from cut import *

def test_case_0():
	cut = calorie_intake_calc(127.53,215.69,67,'M',0.06,'E')
	cut.bodyfat = -0.14
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(42.61,156.17,25,'F',0.65,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.03

def test_case_2():
	cut = calorie_intake_calc(153.2,219.34,82,'F',0.42,'E')
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(158.35,195.49,58,'N',-0.26,'N')

def test_case_4():
	cut = calorie_intake_calc(58.95,213.56,51,'M',0.17,'N')
	cut.age = 5
	cut.weight = 142.83

def test_case_5():
	cut = calorie_intake_calc(156.31,150.44,55,'F',0.24,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.age = 51

