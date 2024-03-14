from cut import *

def test_case_0():
	cut = calorie_intake_calc(178.62,142.71,31,'F',0.13,'L')
	cut.bodyfat = 0.21

def test_case_1():
	cut = calorie_intake_calc(153.54,196.07,24,'F',0.04,'S')
	cut.bodyfat = 0.16
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(168.96,209.4,10,'F',0.16,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()

