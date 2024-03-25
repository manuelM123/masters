from cut import *

def test_case_0():
	cut = calorie_intake_calc(147.14,150.38,68,'M',0.12,'M')
	cut.age = 67
	cut.age = 66
	cut.amount_exercise = 'S'
	cut.height = 152.84
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.17
	cut.weight = 176.86
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(98.72,162.38,31,'F',0.29,'N')
	cut.weight = 203.98
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(198.08,214.94,68,'M',0.01,'L')

def test_case_3():
	cut = calorie_intake_calc(108.12,171.72,18,'F',0.15,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

