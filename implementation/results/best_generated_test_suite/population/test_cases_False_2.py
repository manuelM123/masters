from cut import *

def test_case_0():
	cut = calorie_intake_calc(97.51,175.54,63,'M',0.27,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'

def test_case_1():
	cut = calorie_intake_calc(199.97,150.21,59,'M',0.06,'L')
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(44.69,151.12,72,'N',0.04,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

