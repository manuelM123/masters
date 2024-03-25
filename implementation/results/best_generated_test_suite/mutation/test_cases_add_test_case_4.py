from cut import *

def test_case_0():
	cut = calorie_intake_calc(199.97,173.1,65,'M',0.29,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 187.41
	cut.amount_exercise = 'M'
	cut.weight = 70.57
	cut.bodyfat = 0.27
	cut.height = 153.82
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 201.02

def test_case_1():
	cut = calorie_intake_calc(44.35,160.77,33,'M',0.02,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 178.55
	cut.gender = 'M'
	cut.weight = 80.83
	cut.weight = 168.67
	cut.height = 163.78
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(107.7,164.96,51,'N',0.09,'M')
	cut.gender = 'M'
	cut.age = 55
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 207.85
	cut.gender = 'F'
	cut.weight = 82.22
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 184.7

