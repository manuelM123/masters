from cut import *

def test_case_0():
	cut = calorie_intake_calc(76.68,197.73,39,'M',0.24,'L')
	cut.height = 168.16
	cut.age = 61
	cut.weight = 62.42
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 195.25

def test_case_1():
	cut = calorie_intake_calc(136.3,184.28,61,'F',0.22,'V')

def test_case_2():
	cut = calorie_intake_calc(96.95,173.13,39,'M',0.28,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

