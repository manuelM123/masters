from cut import *

def test_case_0():
	cut = calorie_intake_calc(156.58,205.91,15,'F',0.21,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.19
	cut.gender = 'N'
	cut.bodyfat = 0.2
	cut.bodyfat = 0.0
	cut.weight = 63.04

def test_case_1():
	cut = calorie_intake_calc(113.73,206.37,74,'N',0.1,'V')
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(129.76,184.18,28,'F',0.12,'E')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(121.93,210.33,27,'M',0.13,'V')
	cut.height = 211.62
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 190.58
	cut.age = 63
	cut.age = 24
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.26
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(94.36,167.13,25,'F',0.01,'N')
	cut.weight = 167.51
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 63
	cut.height = 209.77

