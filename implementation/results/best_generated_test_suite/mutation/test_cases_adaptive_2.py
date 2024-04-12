from cut import *

def test_case_0():
	cut = calorie_intake_calc(132.99,168.2,62,'F',0.07,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.13
	cut.age = 50
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 141.25

def test_case_1():
	cut = calorie_intake_calc(200.86,199.9,38,'N',0.16,'V')
	cut.age = 73
	cut.height = 203.48
	cut.bodyfat = 0.27
	cut.age = 49
	cut.weight = 159.12

def test_case_2():
	cut = calorie_intake_calc(199.04,205.39,17,'M',0.19,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'

