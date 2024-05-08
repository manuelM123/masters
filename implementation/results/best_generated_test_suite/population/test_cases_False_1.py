from cut import *

def test_case_0():
	cut = calorie_intake_calc(128.74,223.5,52,'N',0.73,'L')
	cut.bodyfat = 0.25
	cut.age = 32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 154.6
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(87.3,218.66,79,'M',-0.26,'V')
	cut.bodyfat = 0.44
	cut.bodyfat = -0.3
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 39
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 58
	cut.age = 55
	cut.height = 219.1
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 129.93

