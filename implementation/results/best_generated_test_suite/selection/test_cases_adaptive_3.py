from cut import *

def test_case_0():
	cut = calorie_intake_calc(206.21,156.85,29,'F',0.25,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.15
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'E'
	cut.weight = 77.3
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(209.77,208.99,10,'M',0.22,'V')
	cut.bodyfat = 0.11
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(165.98,199.66,73,'M',0.08,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.17
	cut.gender = 'F'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.gender = 'N'

