from cut import *

def test_case_0():
	cut = calorie_intake_calc(176.37,160.2,75,'M',0.18,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(128.3,159.88,13,'F',0.17,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.21
	cut.weight = 206.52
	cut.weight = 116.45
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(132.28,168.89,14,'F',0.23,'L')
	cut.bodyfat = 0.15

def test_case_3():
	cut = calorie_intake_calc(146.34,172.61,50,'M',0.07,'M')
	cut.bodyfat = 0.11
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

