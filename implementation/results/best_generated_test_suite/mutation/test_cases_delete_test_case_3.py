from cut import *

def test_case_0():
	cut = calorie_intake_calc(75.12,179.12,49,'F',0.29,'V')
	cut.height = 206.53
	cut.weight = 118.73
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.age = 56

def test_case_1():
	cut = calorie_intake_calc(178.21,148.18,39,'M',0.27,'N')
	cut.height = 199.34
	cut.bodyfat = 0.08
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(191.54,155.43,28,'N',0.3,'S')
	cut.age = 59
	cut.age = 51
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.07
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 70

def test_case_3():
	cut = calorie_intake_calc(208.54,160.77,45,'F',0.01,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 49.23

