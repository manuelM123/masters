from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	cut.gender = 'M'
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.bodyfat = 0.16
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(151.03,153.56,75,'M',-0.29,'S')
	cut.weight = 93.38

def test_case_2():
	cut = calorie_intake_calc(37.98,144.17,32,'F',0.39,'S')
	cut.bodyfat = 0.28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 207.11
	cut.bodyfat = 0.46

def test_case_3():
	cut = calorie_intake_calc(127.8,158.1,78,'F',0.51,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 21
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(202.51,184.45,53,'M',0.77,'S')
	cut.bodyfat = -0.42
	cut.height = 152.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 150.19

def test_case_5():
	cut = calorie_intake_calc(155.82,216.84,85,'M',0.25,'E')
	cut.age = 46
	cut.weight = 40.08
	cut.bodyfat = 0.67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

