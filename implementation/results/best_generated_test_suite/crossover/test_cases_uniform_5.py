from cut import *

def test_case_0():
	cut = calorie_intake_calc(70.17,174.89,62,'F',0.26,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 76.13
	cut.age = 58
	cut.height = 143.87
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(75.79,153.79,57,'F',0.25,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 168.06
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(128.41,191.82,28,'F',0.06,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(68.6,183.68,51,'F',0.01,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.16
	cut.gender = 'N'
	cut.amount_exercise = 'E'
	cut.age = 43
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(125.62,193.31,62,'N',0.2,'M')

