from cut import *

def test_case_0():
	cut = calorie_intake_calc(173.01,147.94,34,'N',0.26,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(153.29,148.19,46,'N',0.1,'L')
	cut.weight = 176.43
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 52

def test_case_2():
	cut = calorie_intake_calc(194.57,160.15,67,'M',0.13,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(74.58,180.45,57,'N',0.07,'V')
	cut.age = 19
	result_determine_calorie_intake = cut.determine_calorie_intake()

