from cut import *

def test_case_0():
	cut = calorie_intake_calc(170.57,155.77,79,'M',0.17,'S')
	cut.age = 23
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 44
	cut.gender = 'F'
	cut.amount_exercise = 'S'

def test_case_1():
	cut = calorie_intake_calc(49.44,147.83,81,'M',0.05,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.07
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 14
	cut.age = 39

def test_case_2():
	cut = calorie_intake_calc(120.94,164.8,75,'F',0.12,'V')
	cut.bodyfat = 0.1
	cut.age = 52
	cut.height = 166.92
	cut.bodyfat = 0.04
	cut.age = 59
	cut.height = 219.47
	cut.bodyfat = 0.14
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(141.95,215.36,37,'M',0.28,'V')
	cut.weight = 68.48
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.26

def test_case_4():
	cut = calorie_intake_calc(60.26,194.25,51,'M',0.11,'L')
	cut.weight = 62.71
	cut.bodyfat = 0.18

