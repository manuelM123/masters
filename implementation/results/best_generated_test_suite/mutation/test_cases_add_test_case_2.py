from cut import *

def test_case_0():
	cut = calorie_intake_calc(81.92,160.15,75,'F',0.26,'V')
	cut.height = 157.01
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 45

def test_case_1():
	cut = calorie_intake_calc(105.86,194.32,69,'N',0.04,'N')
	cut.height = 206.45
	cut.bodyfat = 0.0
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 176.27

