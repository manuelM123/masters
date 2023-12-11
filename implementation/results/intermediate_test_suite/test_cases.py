from cut import *

def test_case_0():
	cut = calorie_intake_calc(92.64,160.0,80,'N',0.25,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 196.27
	cut.amount_exercise = 'L'

def test_case_1():
	cut = calorie_intake_calc(94.25,177.98,46,'M',0.27,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 216.78
	cut.amount_exercise = 'V'

def test_case_2():
	cut = calorie_intake_calc(186.66,162.11,27,'M',0.1,'N')
	cut.height = 176.89
	cut.age = 68
	cut.amount_exercise = 'N'

