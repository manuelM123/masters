from cut import *

def test_case_0():
	cut = calorie_intake_calc(102.2,176.44,18,'M',0.19,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.13

def test_case_1():
	cut = calorie_intake_calc(47.56,160.84,64,'F',0.02,'V')
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 54
	cut.age = 47
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.bodyfat = 0.08

