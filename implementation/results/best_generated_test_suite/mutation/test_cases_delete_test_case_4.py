from cut import *

def test_case_0():
	cut = calorie_intake_calc(69.98,169.07,68,'M',-0.3,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.height = 196.25

def test_case_1():
	cut = calorie_intake_calc(204.96,221.43,79,'N',-0.24,'E')

