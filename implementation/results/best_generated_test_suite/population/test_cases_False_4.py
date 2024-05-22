from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 56.81
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.3
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 38
	cut.weight = 112.51

def test_case_1():
	cut = calorie_intake_calc(140.85,146.01,40,'F',0.42,'S')
	cut.gender = 'M'
	cut.height = 136.94
	cut.bodyfat = 0.24

def test_case_2():
	cut = calorie_intake_calc(40.77,155.29,62,'M',-0.17,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

