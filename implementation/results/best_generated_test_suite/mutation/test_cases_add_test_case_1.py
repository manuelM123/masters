from cut import *

def test_case_0():
	cut = calorie_intake_calc(144.24,201.1,26,'M',0.21,'E')
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(166.28,172.89,42,'M',0.21,'V')

