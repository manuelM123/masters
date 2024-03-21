from cut import *

def test_case_0():
	cut = calorie_intake_calc(89.61,205.01,26,'N',0.02,'L')

def test_case_1():
	cut = calorie_intake_calc(192.65,180.4,30,'N',0.28,'N')
	cut.height = 148.87
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

