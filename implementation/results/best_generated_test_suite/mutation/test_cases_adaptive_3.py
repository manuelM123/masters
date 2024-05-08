from cut import *

def test_case_0():
	cut = calorie_intake_calc(150.98,214.07,73,'F',0.11,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 130.88
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 142.44
	cut.amount_exercise = 'E'

def test_case_1():
	cut = calorie_intake_calc(117.82,153.16,13,'M',-0.22,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.bodyfat = -0.17
	cut.gender = 'N'
	cut.weight = 36.16
	cut.gender = 'F'
	cut.height = 155.43
	cut.weight = 199.69

