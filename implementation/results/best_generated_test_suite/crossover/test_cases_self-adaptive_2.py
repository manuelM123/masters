from cut import *

def test_case_0():
	cut = calorie_intake_calc(178.95,160.58,34,'M',0.17,'S')

def test_case_1():
	cut = calorie_intake_calc(51.15,152.97,66,'F',0.22,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.04
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

