from cut import *

def test_case_0():
	cut = calorie_intake_calc(119.74,144.69,13,'M',0.06,'N')
	cut.bodyfat = 0.13

def test_case_1():
	cut = calorie_intake_calc(175.45,190.56,76,'M',0.19,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 52
	cut.height = 178.4
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.17
	result_tdee_calculation = cut.tdee_calculation()

