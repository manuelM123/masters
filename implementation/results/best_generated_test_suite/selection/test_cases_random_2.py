from cut import *

def test_case_0():
	cut = calorie_intake_calc(148.13,177.16,13,'N',0.2,'S')

def test_case_1():
	cut = calorie_intake_calc(52.08,182.67,41,'F',0.0,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

