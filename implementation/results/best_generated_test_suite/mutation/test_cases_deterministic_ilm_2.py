from cut import *

def test_case_0():
	cut = calorie_intake_calc(87.41,188.63,68,'F',0.25,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(150.32,198.98,12,'F',0.12,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.height = 174.72

def test_case_2():
	cut = calorie_intake_calc(59.54,158.39,57,'N',0.09,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.18

