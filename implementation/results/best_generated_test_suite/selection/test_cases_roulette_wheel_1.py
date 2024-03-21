from cut import *

def test_case_0():
	cut = calorie_intake_calc(182.4,146.28,38,'F',0.07,'V')
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 22

def test_case_1():
	cut = calorie_intake_calc(199.41,179.91,18,'M',0.2,'L')
	cut.amount_exercise = 'N'
	cut.bodyfat = 0.24
	cut.gender = 'M'
	cut.height = 161.14

