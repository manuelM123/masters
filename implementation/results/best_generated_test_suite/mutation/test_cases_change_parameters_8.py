from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.bodyfat = 0.16
	cut.bodyfat = 0.7

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.weight = 126.4

def test_case_2():
	cut = calorie_intake_calc(39.96,215.29,22,'F',0.39,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46
	cut.amount_exercise = 'V'
	cut.height = 203.78
	cut.weight = 128.03

def test_case_3():
	cut = calorie_intake_calc(157.95,205.75,19,'F',0.59,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.bodyfat = 0.76
	cut.weight = 86.55
	cut.age = 20
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.02

def test_case_4():
	cut = calorie_intake_calc(91.03,219.41,16,'M',0.8,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

