from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	cut.gender = 'M'
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.age = 38
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(167.13,188.43,53,'F',-0.24,'L')
	cut.age = 35
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 165.29
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 174.15
	cut.weight = 39.3

