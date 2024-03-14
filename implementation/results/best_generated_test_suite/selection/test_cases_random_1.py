from cut import *

def test_case_0():
	cut = calorie_intake_calc(117.0,171.58,66,'F',0.03,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.height = 188.68

def test_case_1():
	cut = calorie_intake_calc(109.92,198.03,35,'F',0.23,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.22

def test_case_2():
	cut = calorie_intake_calc(135.81,214.3,43,'N',0.15,'E')
	cut.age = 76

