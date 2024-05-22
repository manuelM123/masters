from cut import *

def test_case_0():
	cut = calorie_intake_calc(151.1,210.7,60,'M',-0.1,'M')
	cut.height = 150.46
	cut.bodyfat = -0.32
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 60
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.16
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(167.13,188.43,53,'F',-0.24,'L')
	cut.age = 35
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 165.29
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 174.15
	cut.weight = 39.3

def test_case_3():
	cut = calorie_intake_calc(112.09,164.47,8,'F',-0.45,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.48
	cut.weight = 43.94
	cut.height = 136.53

