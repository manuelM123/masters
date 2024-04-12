from cut import *

def test_case_0():
	cut = calorie_intake_calc(55.93,207.94,54,'M',0.09,'E')
	cut.amount_exercise = 'L'
	cut.weight = 52.62
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 172.02
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.13

def test_case_1():
	cut = calorie_intake_calc(198.56,217.38,16,'F',0.04,'N')
	cut.bodyfat = 0.27

def test_case_2():
	cut = calorie_intake_calc(79.11,205.99,24,'M',0.17,'E')
	cut.weight = 147.62
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.22
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.11
	cut.amount_exercise = 'V'

