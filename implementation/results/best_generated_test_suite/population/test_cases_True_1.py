from cut import *

def test_case_0():
	cut = calorie_intake_calc(127.64,145.92,35,'M',0.12,'V')
	cut.bodyfat = 0.28

def test_case_1():
	cut = calorie_intake_calc(126.3,164.07,29,'N',0.22,'L')
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

