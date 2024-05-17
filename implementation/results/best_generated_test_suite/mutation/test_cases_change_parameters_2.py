from cut import *

def test_case_0():
	cut = calorie_intake_calc(42.25,149.0,82,'F',-0.46,'S')
	cut.bodyfat = -0.08
	cut.amount_exercise = 'L'
	cut.weight = 66.37

def test_case_1():
	cut = calorie_intake_calc(76.05,183.52,43,'F',-0.44,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 180.07
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'

