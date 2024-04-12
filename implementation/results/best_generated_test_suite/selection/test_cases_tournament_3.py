from cut import *

def test_case_0():
	cut = calorie_intake_calc(167.56,204.23,40,'N',0.29,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 187.15
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(124.22,163.84,19,'M',0.01,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(108.38,158.48,36,'N',0.23,'M')
	cut.weight = 194.24
	cut.bodyfat = 0.27
	cut.weight = 127.64
	cut.weight = 110.7
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.21
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(107.95,178.11,69,'M',0.05,'L')
	cut.amount_exercise = 'E'
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 31
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.gender = 'N'

