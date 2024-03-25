from cut import *

def test_case_0():
	cut = calorie_intake_calc(120.23,189.76,46,'M',0.11,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(201.78,216.85,42,'M',0.07,'E')
	cut.weight = 171.29
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 30
	cut.weight = 42.18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(155.13,171.65,56,'M',0.1,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(63.46,174.45,60,'F',0.0,'N')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.24

