from cut import *

def test_case_0():
	cut = calorie_intake_calc(53.87,204.18,28,'F',0.3,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(147.65,147.87,55,'M',-0.37,'V')
	cut.weight = 58.75
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(81.13,202.26,34,'M',-0.13,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

