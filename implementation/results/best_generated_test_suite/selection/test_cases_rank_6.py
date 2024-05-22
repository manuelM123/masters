from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	cut.gender = 'M'
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.bodyfat = -0.0
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.bodyfat = 0.16
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(184.34,144.5,5,'N',-0.08,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.57
	cut.age = 36
	cut.height = 203.78
	cut.weight = 128.03

def test_case_3():
	cut = calorie_intake_calc(197.63,188.28,52,'N',0.67,'E')
	cut.amount_exercise = 'V'
	cut.bodyfat = -0.48
	cut.weight = 43.94
	cut.height = 136.53

