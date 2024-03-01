from cut import *

def test_case_0():
	cut = calorie_intake_calc(51.24,160.89,58,'N',0.05,'E')
	cut.gender = 'F'
	cut.height = 142.26
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(154.56,174.04,39,'N',0.25,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(69.02,141.77,74,'M',0.15,'E')
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.25
	cut.bodyfat = 0.14

def test_case_3():
	cut = calorie_intake_calc(98.88,175.59,39,'N',0.26,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 194.84

