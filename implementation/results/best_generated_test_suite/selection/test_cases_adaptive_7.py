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
	cut = calorie_intake_calc(73.72,211.22,28,'M',0.04,'S')
	cut.age = 77
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 197.51
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.73
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 56

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

def test_case_3():
	cut = calorie_intake_calc(95.65,215.72,44,'F',0.11,'L')
	cut.bodyfat = 0.1
	result_tdee_calculation = cut.tdee_calculation()

