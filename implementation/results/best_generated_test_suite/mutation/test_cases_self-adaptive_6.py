from cut import *

def test_case_0():
	cut = calorie_intake_calc(179.25,157.48,64,'F',0.2,'L')
	cut.weight = 36.1
	cut.weight = 196.8
	cut.weight = 139.46

def test_case_1():
	cut = calorie_intake_calc(108.57,151.92,34,'M',0.24,'V')
	cut.bodyfat = 0.07
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 84
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.31

