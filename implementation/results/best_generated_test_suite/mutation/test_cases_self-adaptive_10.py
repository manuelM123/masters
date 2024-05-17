from cut import *

def test_case_0():
	cut = calorie_intake_calc(115.23,158.09,84,'M',-0.34,'E')
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(163.24,200.62,5,'N',0.49,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(196.71,152.85,49,'F',0.39,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 15

def test_case_3():
	cut = calorie_intake_calc(109.8,222.18,58,'N',0.34,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.1
	cut.age = 5
	cut.height = 158.72
	cut.height = 180.48
	cut.height = 170.23
	cut.gender = 'N'
	cut.height = 171.77
	cut.height = 221.99
	cut.bodyfat = 0.26

def test_case_4():
	cut = calorie_intake_calc(132.42,188.19,78,'N',0.79,'L')
	cut.age = 15
	cut.bodyfat = 0.58
	cut.height = 183.34
	cut.amount_exercise = 'E'

def test_case_5():
	cut = calorie_intake_calc(136.13,173.24,30,'M',-0.47,'V')
	cut.height = 150.97
	cut.amount_exercise = 'E'
	cut.weight = 165.21
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.06
	cut.weight = 37.14
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.78

def test_case_6():
	cut = calorie_intake_calc(149.68,160.33,20,'N',-0.16,'L')
	cut.age = 71
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 35
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

