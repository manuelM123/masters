from cut import *

def test_case_0():
	cut = calorie_intake_calc(194.11,187.13,54,'F',0.05,'V')

def test_case_1():
	cut = calorie_intake_calc(61.17,160.52,37,'N',0.11,'E')
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 93.53

