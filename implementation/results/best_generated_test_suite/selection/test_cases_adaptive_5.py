from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.96,151.8,70,'F',0.29,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.weight = 40.65
	cut.weight = 86.9
	cut.weight = 210.92
	cut.height = 158.72
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(73.72,211.22,28,'M',0.04,'S')
	cut.age = 77
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 197.51
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.73
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 56

def test_case_2():
	cut = calorie_intake_calc(145.82,210.41,65,'F',0.22,'S')
	cut.weight = 46.77
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 212.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'

