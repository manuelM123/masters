from cut import *

def test_case_0():
	cut = calorie_intake_calc(166.26,174.85,16,'F',0.19,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(208.59,188.99,23,'M',0.2,'S')

def test_case_2():
	cut = calorie_intake_calc(170.17,149.25,40,'N',0.01,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 203.67
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(135.68,153.49,20,'M',0.2,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

