from cut import *

def test_case_0():
	cut = calorie_intake_calc(123.0,151.9,45,'M',0.64,'M')
	cut.height = 179.92
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 185.98

