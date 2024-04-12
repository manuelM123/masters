from cut import *

def test_case_0():
	cut = calorie_intake_calc(166.72,172.0,13,'M',0.29,'M')
	cut.amount_exercise = 'S'
	cut.gender = 'N'
	cut.gender = 'F'
	cut.age = 39
	cut.bodyfat = 0.02
	cut.bodyfat = 0.04
	cut.age = 16
	cut.bodyfat = 0.19
	cut.weight = 86.79
	cut.amount_exercise = 'N'

def test_case_1():
	cut = calorie_intake_calc(167.65,168.56,45,'M',0.23,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 147.62
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 168.48
	cut.gender = 'M'
	cut.age = 54

