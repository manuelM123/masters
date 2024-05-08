from cut import *

def test_case_0():
	cut = calorie_intake_calc(103.21,213.38,10,'M',0.62,'S')

def test_case_1():
	cut = calorie_intake_calc(139.24,213.07,83,'N',0.41,'V')
	cut.gender = 'F'
	cut.age = 50
	cut.age = 42
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(43.1,185.31,77,'M',-0.49,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.27
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 193.04
	cut.height = 209.88
	cut.age = 14
	result_determine_calorie_intake = cut.determine_calorie_intake()

