from cut import *

def test_case_0():
	cut = calorie_intake_calc(82.36,144.36,78,'M',0.08,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 149.84
	cut.bodyfat = 0.22
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(172.81,177.73,81,'M',0.28,'V')
	cut.bodyfat = 0.14
	cut.gender = 'F'
	cut.bodyfat = 0.14
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(40.78,184.56,24,'F',0.13,'M')
	cut.bodyfat = 0.02
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()

