from cut import *

def test_case_0():
	cut = calorie_intake_calc(69.64,206.46,55,'M',0.29,'S')

def test_case_1():
	cut = calorie_intake_calc(91.87,190.85,40,'M',0.12,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.12
	cut.weight = 197.09
	cut.gender = 'F'
	cut.age = 35

def test_case_2():
	cut = calorie_intake_calc(144.14,177.6,63,'F',0.29,'E')
	cut.bodyfat = 0.25
	cut.age = 78
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.1
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(185.04,146.17,47,'N',0.04,'E')
	cut.height = 146.81
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.13
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 80
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

