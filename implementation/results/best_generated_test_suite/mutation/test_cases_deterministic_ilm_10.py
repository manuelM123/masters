from cut import *

def test_case_0():
	cut = calorie_intake_calc(36.96,224.79,83,'N',-0.37,'L')
	cut.amount_exercise = 'L'
	cut.age = 36
	cut.height = 166.85
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(129.62,164.76,20,'M',0.02,'N')
	cut.gender = 'N'
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 174.46
	cut.amount_exercise = 'M'
	cut.age = 61
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(100.77,159.35,76,'M',-0.42,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.77
	cut.weight = 116.18
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.13

def test_case_3():
	cut = calorie_intake_calc(181.97,200.97,29,'M',0.25,'V')
	cut.bodyfat = -0.49
	cut.gender = 'F'
	cut.weight = 86.14
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'

