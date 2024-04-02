from cut import *

def test_case_0():
	cut = calorie_intake_calc(116.99,187.92,62,'N',0.13,'V')
	cut.age = 47
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(118.72,162.05,48,'N',0.21,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(160.39,207.34,65,'M',0.26,'S')
	result_tdee_calculation = cut.tdee_calculation()

