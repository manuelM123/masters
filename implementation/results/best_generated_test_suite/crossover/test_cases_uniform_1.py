from cut import *

def test_case_0():
	cut = calorie_intake_calc(107.02,209.11,17,'F',0.04,'V')
	cut.weight = 181.87
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 105.3
	cut.weight = 118.63

def test_case_1():
	cut = calorie_intake_calc(115.61,170.68,26,'F',0.19,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'

def test_case_2():
	cut = calorie_intake_calc(88.31,194.2,28,'F',0.09,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

