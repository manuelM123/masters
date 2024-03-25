from cut import *

def test_case_0():
	cut = calorie_intake_calc(93.94,161.48,66,'M',0.28,'N')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 138.53
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 89.84
	cut.height = 199.46
	cut.gender = 'M'
	cut.gender = 'N'
	cut.bodyfat = 0.17
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(101.88,212.12,32,'M',0.1,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 119.39
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(187.96,219.02,52,'F',0.23,'E')
	cut.weight = 180.86
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 60
	cut.weight = 68.3
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 210.47
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(165.23,185.13,80,'N',0.0,'V')
	cut.height = 150.24
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 215.34

def test_case_4():
	cut = calorie_intake_calc(188.99,158.92,49,'N',0.01,'S')
	cut.gender = 'F'
	cut.bodyfat = 0.18

