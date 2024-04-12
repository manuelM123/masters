from cut import *

def test_case_0():
	cut = calorie_intake_calc(119.77,154.85,67,'F',0.05,'M')
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 15
	cut.height = 200.82
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(115.6,176.29,79,'F',0.02,'L')
	cut.gender = 'F'
	cut.gender = 'N'
	cut.height = 176.86

def test_case_2():
	cut = calorie_intake_calc(121.04,203.84,31,'F',0.07,'L')
	cut.weight = 112.65
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 197.03
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(167.16,219.06,77,'M',0.11,'E')
	cut.weight = 167.82
	cut.height = 155.35
	cut.bodyfat = 0.07
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(120.99,185.32,15,'F',0.16,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

