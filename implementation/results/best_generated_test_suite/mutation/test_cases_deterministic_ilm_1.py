from cut import *

def test_case_0():
	cut = calorie_intake_calc(98.91,205.17,78,'N',0.14,'N')
	cut.bodyfat = 0.27
	cut.age = 79
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 52.29
	cut.gender = 'N'
	cut.amount_exercise = 'S'

def test_case_1():
	cut = calorie_intake_calc(202.89,155.99,51,'M',0.2,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.16
	cut.gender = 'M'
	cut.weight = 132.63

