from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.56,212.61,14,'M',-0.43,'V')
	cut.height = 147.0
	cut.bodyfat = 0.12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 141.42

def test_case_1():
	cut = calorie_intake_calc(142.51,187.51,66,'M',-0.03,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(62.73,220.7,36,'M',-0.06,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 174.75

