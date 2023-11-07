from cut import *

def test_case_0():
	cut = calorie_intake_calc(71.26,163.74,55,'M',0.25,'V')
	cut.bodyfat = 0.16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.09

def test_case_1():
	cut = calorie_intake_calc(180.29,186.63,69,'M',0.13,'M')
	cut.bodyfat = 0.22
	cut.bodyfat = 0.17

def test_case_2():
	cut = calorie_intake_calc(207.75,158.48,30,'F',0.01,'S')

