from cut import *

def test_case_0():
	cut = calorie_intake_calc(107.25,145.61,24,'F',0.17,'M')

def test_case_1():
	cut = calorie_intake_calc(48.07,190.56,81,'M',0.03,'N')

def test_case_2():
	cut = calorie_intake_calc(165.63,161.02,69,'N',0.18,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 177.44
	cut.height = 164.39
	cut.gender = 'F'
	cut.height = 171.9
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 14
	cut.weight = 143.76

def test_case_3():
	cut = calorie_intake_calc(137.04,218.74,34,'F',0.11,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 173.5
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(115.41,214.35,47,'F',0.26,'M')
	cut.age = 11
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.weight = 42.41

