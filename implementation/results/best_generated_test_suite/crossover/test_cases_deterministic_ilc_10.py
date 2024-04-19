from cut import *

def test_case_0():
	cut = calorie_intake_calc(72.59,163.75,17,'N',0.25,'M')
	cut.gender = 'F'
	cut.age = 71
	cut.age = 69
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(135.54,184.84,13,'N',0.2,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'S'
	cut.height = 178.07

def test_case_2():
	cut = calorie_intake_calc(161.65,207.41,59,'F',0.28,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 197.63
	cut.gender = 'N'
	cut.weight = 66.65

def test_case_3():
	cut = calorie_intake_calc(49.32,199.1,18,'F',0.04,'M')
	cut.bodyfat = 0.02
	cut.height = 157.43
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'

def test_case_4():
	cut = calorie_intake_calc(107.15,200.72,37,'M',0.25,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 67
	cut.age = 78
	cut.age = 35
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 148.95
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

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
	cut = calorie_intake_calc(49.98,210.05,78,'F',0.1,'M')
	cut.height = 153.78
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 211.1

