from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.61,217.84,60,'M',-0.44,'V')
	cut.weight = 106.24
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.28
	cut.height = 222.02
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.01

def test_case_1():
	cut = calorie_intake_calc(192.7,177.0,7,'F',-0.36,'V')
	cut.bodyfat = 0.21
	cut.amount_exercise = 'S'
	cut.age = 69
	cut.amount_exercise = 'M'
	cut.gender = 'N'
	cut.weight = 101.06
	cut.bodyfat = 0.16
	cut.bodyfat = -0.1
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

