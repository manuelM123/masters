from cut import *

def test_case_0():
	cut = calorie_intake_calc(204.32,147.45,74,'M',0.12,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.weight = 147.27

def test_case_1():
	cut = calorie_intake_calc(179.49,196.57,34,'M',0.1,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(140.76,181.26,49,'N',0.07,'N')
	cut.height = 209.28
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(201.2,213.7,24,'M',0.16,'E')
	cut.amount_exercise = 'M'
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 74.61
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.04
	cut.age = 23
	cut.gender = 'N'

