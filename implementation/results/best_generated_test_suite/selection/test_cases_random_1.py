from cut import *

def test_case_0():
	cut = calorie_intake_calc(81.92,160.15,75,'F',0.26,'V')
	cut.height = 157.01
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 45

def test_case_1():
	cut = calorie_intake_calc(175.71,220.86,48,'M',0.12,'M')
	cut.age = 75

