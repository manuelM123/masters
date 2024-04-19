from cut import *

def test_case_0():
	cut = calorie_intake_calc(210.89,199.49,41,'N',0.26,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 208.58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(135.54,184.84,13,'N',0.2,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'S'
	cut.height = 178.07

def test_case_2():
	cut = calorie_intake_calc(145.82,210.41,65,'F',0.22,'S')
	cut.weight = 46.77
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 212.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'

def test_case_3():
	cut = calorie_intake_calc(125.81,165.41,67,'N',0.22,'M')
	cut.height = 174.28

def test_case_4():
	cut = calorie_intake_calc(199.53,161.63,22,'F',0.29,'L')
	cut.weight = 51.27
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.height = 174.79
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 192.06
	cut.height = 190.6
	cut.age = 33
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(120.04,151.1,41,'M',0.23,'L')
	cut.amount_exercise = 'M'
	cut.gender = 'M'
	cut.bodyfat = 0.17
	cut.weight = 127.14
	cut.age = 19
	cut.age = 13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.04

def test_case_6():
	cut = calorie_intake_calc(70.58,156.97,20,'F',0.12,'E')
	cut.height = 196.09
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.height = 206.76
	result_determine_calorie_intake = cut.determine_calorie_intake()

