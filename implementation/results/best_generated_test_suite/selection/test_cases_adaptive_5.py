from cut import *

def test_case_0():
	cut = calorie_intake_calc(191.69,143.78,39,'M',0.0,'N')
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	cut.age = 75
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 166.28

def test_case_1():
	cut = calorie_intake_calc(51.18,215.2,15,'M',0.07,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 196.5
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 60.06

def test_case_2():
	cut = calorie_intake_calc(166.32,142.76,66,'M',0.05,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.age = 81
	cut.height = 140.35
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 68.37

