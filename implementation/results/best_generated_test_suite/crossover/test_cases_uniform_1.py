from cut import *

def test_case_0():
	cut = calorie_intake_calc(107.29,144.04,68,'F',0.07,'E')
	cut.age = 22
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 79
	cut.bodyfat = 0.21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 19

def test_case_1():
	cut = calorie_intake_calc(136.46,161.61,73,'F',0.18,'L')

def test_case_2():
	cut = calorie_intake_calc(142.65,165.18,11,'M',0.12,'N')
	cut.height = 140.23
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 211.56
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 84.9
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.age = 11

