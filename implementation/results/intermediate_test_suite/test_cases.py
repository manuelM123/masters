from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.76,199.67,54,'F',0.25,'V')
	cut.weight = 89.18
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(73.39,199.17,21,'M',0.13,'S')
	cut.gender = 'M'
	cut.amount_exercise = 'V'

def test_case_2():
	cut = calorie_intake_calc(180.95,179.51,39,'M',0.03,'L')
	cut.weight = 189.36

