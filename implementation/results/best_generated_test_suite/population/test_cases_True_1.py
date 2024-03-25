from cut import *

def test_case_0():
	cut = calorie_intake_calc(160.5,182.44,77,'F',0.14,'L')
	cut.age = 13
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.29
	cut.amount_exercise = 'N'

def test_case_1():
	cut = calorie_intake_calc(200.13,205.3,30,'N',0.17,'M')
	cut.age = 10
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(121.43,148.98,67,'M',0.03,'E')
	cut.age = 13
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.height = 152.04
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(208.01,160.12,71,'M',0.1,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(172.85,218.62,21,'N',0.18,'S')
	cut.amount_exercise = 'S'
	cut.age = 61
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 152.89
	cut.bodyfat = 0.09
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'

