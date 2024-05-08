from cut import *

def test_case_0():
	cut = calorie_intake_calc(54.36,195.63,24,'M',0.73,'L')

def test_case_1():
	cut = calorie_intake_calc(95.77,149.41,36,'F',0.14,'S')
	cut.height = 186.46
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(124.88,182.68,13,'M',0.25,'E')
	cut.age = 27
	cut.height = 173.07
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.77

