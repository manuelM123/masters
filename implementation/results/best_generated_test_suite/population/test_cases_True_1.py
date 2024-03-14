from cut import *

def test_case_0():
	cut = calorie_intake_calc(55.42,194.27,72,'M',0.03,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 183.34
	cut.height = 169.49
	cut.age = 72

def test_case_1():
	cut = calorie_intake_calc(208.6,194.15,78,'F',0.24,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

