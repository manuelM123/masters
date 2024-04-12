from cut import *

def test_case_0():
	cut = calorie_intake_calc(153.99,173.92,40,'M',0.01,'S')
	cut.gender = 'N'
	cut.amount_exercise = 'L'

def test_case_1():
	cut = calorie_intake_calc(199.25,178.73,36,'N',0.29,'S')
	cut.age = 33
	cut.age = 31
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.69
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(82.97,180.79,40,'M',0.11,'M')
	cut.age = 40
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.03
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(61.28,189.39,74,'M',0.24,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'

