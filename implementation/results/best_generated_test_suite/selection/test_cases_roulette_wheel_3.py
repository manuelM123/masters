from cut import *

def test_case_0():
	cut = calorie_intake_calc(173.29,166.9,71,'M',0.15,'L')
	cut.weight = 71.72
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 25
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(157.96,201.11,62,'N',0.16,'V')
	cut.age = 57
	cut.height = 215.3
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 160.45

def test_case_2():
	cut = calorie_intake_calc(98.96,185.59,30,'F',0.08,'L')
	cut.age = 42
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 10
	cut.bodyfat = 0.0
	cut.height = 187.68
	cut.bodyfat = 0.2

def test_case_3():
	cut = calorie_intake_calc(173.01,182.26,28,'N',0.2,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.18
	cut.weight = 75.51
	cut.bodyfat = 0.3
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.01
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

