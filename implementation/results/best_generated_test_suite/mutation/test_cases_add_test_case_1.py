from cut import *

def test_case_0():
	cut = calorie_intake_calc(169.99,164.28,13,'F',0.22,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'

def test_case_1():
	cut = calorie_intake_calc(132.09,169.62,51,'F',0.15,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(61.81,180.12,42,'N',0.07,'V')
	cut.age = 73
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

