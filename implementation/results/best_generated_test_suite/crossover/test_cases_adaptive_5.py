from cut import *

def test_case_0():
	cut = calorie_intake_calc(208.02,191.96,20,'F',0.14,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.02
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(121.88,184.23,44,'M',0.11,'L')
	cut.amount_exercise = 'E'
	cut.age = 21
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

