from cut import *

def test_case_0():
	cut = calorie_intake_calc(178.83,136.91,20,'F',0.25,'V')
	cut.height = 173.96
	cut.gender = 'N'
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(56.2,213.18,56,'M',0.08,'M')
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(208.98,140.45,37,'F',-0.2,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 195.1
	cut.height = 205.14
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

