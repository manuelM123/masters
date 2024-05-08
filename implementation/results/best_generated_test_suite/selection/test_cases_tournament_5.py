from cut import *

def test_case_0():
	cut = calorie_intake_calc(84.17,183.49,56,'F',-0.16,'V')

def test_case_1():
	cut = calorie_intake_calc(90.39,154.93,47,'M',-0.01,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.09
	cut.height = 149.43
	cut.bodyfat = 0.13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

