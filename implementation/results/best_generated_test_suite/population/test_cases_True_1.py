from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.08,141.29,65,'F',0.12,'N')
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(210.4,188.0,65,'F',0.23,'N')

def test_case_2():
	cut = calorie_intake_calc(135.83,216.21,62,'M',0.05,'V')

def test_case_3():
	cut = calorie_intake_calc(184.6,167.92,17,'F',0.18,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 164.26
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 32

def test_case_4():
	cut = calorie_intake_calc(99.53,218.91,22,'M',0.05,'S')
	cut.bodyfat = 0.13
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.weight = 61.79
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 147.22
	cut.bodyfat = 0.27
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

