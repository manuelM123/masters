from cut import *

def test_case_0():
	cut = calorie_intake_calc(199.4,211.39,69,'M',-0.13,'E')
	cut.height = 167.31
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 9
	cut.age = 15

def test_case_1():
	cut = calorie_intake_calc(111.61,211.43,30,'F',0.03,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.38
	cut.age = 66

