from cut import *

def test_case_0():
	cut = calorie_intake_calc(112.58,217.27,36,'N',0.3,'V')
	cut.height = 171.88
	cut.bodyfat = 0.16

def test_case_1():
	cut = calorie_intake_calc(60.38,161.4,52,'F',0.04,'M')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 14
	cut.age = 20

