from cut import *

def test_case_0():
	cut = calorie_intake_calc(81.92,160.15,75,'F',0.26,'V')
	cut.height = 157.01
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 45

def test_case_1():
	cut = calorie_intake_calc(107.41,157.82,51,'N',0.23,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

