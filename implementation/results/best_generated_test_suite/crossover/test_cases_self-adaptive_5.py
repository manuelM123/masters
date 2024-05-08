from cut import *

def test_case_0():
	cut = calorie_intake_calc(51.83,141.78,7,'F',0.71,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(168.97,216.95,54,'M',-0.31,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 36.1
	cut.height = 194.3
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.05
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(123.68,222.48,37,'M',0.42,'N')

def test_case_3():
	cut = calorie_intake_calc(140.29,172.35,52,'F',-0.12,'N')
	cut.height = 158.24
	cut.bodyfat = 0.11
	cut.age = 68
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(199.67,151.55,63,'N',0.38,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 77
	cut.bodyfat = -0.04
	cut.height = 209.94
	cut.amount_exercise = 'M'
	cut.gender = 'F'
	cut.amount_exercise = 'N'

def test_case_5():
	cut = calorie_intake_calc(40.52,206.88,60,'M',-0.22,'V')
	cut.gender = 'M'
	cut.weight = 113.04
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 181.14
	cut.height = 194.52
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.weight = 144.95
	cut.weight = 122.22

