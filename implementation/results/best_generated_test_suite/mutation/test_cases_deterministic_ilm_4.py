from cut import *

def test_case_0():
	cut = calorie_intake_calc(78.32,204.01,11,'F',0.42,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.2
	cut.weight = 55.05
	cut.gender = 'N'
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.0
	cut.height = 184.19

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(111.51,192.81,85,'F',-0.25,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 213.48

def test_case_3():
	cut = calorie_intake_calc(197.63,188.28,52,'N',0.67,'E')
	cut.amount_exercise = 'V'
	cut.bodyfat = -0.48
	cut.weight = 43.94
	cut.height = 136.53

def test_case_4():
	cut = calorie_intake_calc(112.12,153.12,40,'M',-0.21,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.06
	cut.gender = 'N'
	cut.height = 168.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

