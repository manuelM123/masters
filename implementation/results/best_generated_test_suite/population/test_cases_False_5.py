from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	cut.gender = 'M'
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 75.69
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.bodyfat = 0.16
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(129.39,200.26,44,'F',0.3,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.53
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(184.34,144.5,5,'N',-0.08,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.57
	cut.bodyfat = 0.16
	cut.gender = 'F'
	cut.weight = 128.03

def test_case_3():
	cut = calorie_intake_calc(43.86,155.68,40,'M',0.6,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 143.3
	cut.bodyfat = -0.16
	cut.weight = 72.67
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 23
	cut.bodyfat = 0.64
	cut.bodyfat = 0.08
	cut.gender = 'M'

