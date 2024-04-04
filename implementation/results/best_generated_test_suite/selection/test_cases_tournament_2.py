from cut import *

def test_case_0():
	cut = calorie_intake_calc(120.01,186.24,26,'M',0.18,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(93.35,178.51,61,'M',0.05,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(129.92,156.63,33,'M',0.15,'V')
	cut.gender = 'M'

