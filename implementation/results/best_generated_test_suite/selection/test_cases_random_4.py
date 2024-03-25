from cut import *

def test_case_0():
	cut = calorie_intake_calc(83.89,184.37,48,'M',0.17,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 35
	cut.height = 192.48
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.bodyfat = 0.04

def test_case_1():
	cut = calorie_intake_calc(181.01,155.17,47,'F',0.01,'L')
	cut.bodyfat = 0.03
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 216.52
	cut.age = 24
	cut.age = 54
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.1
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(181.05,158.11,60,'M',0.22,'L')
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 159.77
	cut.gender = 'N'
	cut.height = 186.71
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(195.67,201.15,55,'M',0.17,'E')
	cut.bodyfat = 0.06
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.29
	cut.weight = 51.51
	cut.age = 50
	cut.age = 62
	cut.weight = 98.96
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

