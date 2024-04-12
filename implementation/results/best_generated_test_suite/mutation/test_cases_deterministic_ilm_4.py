from cut import *

def test_case_0():
	cut = calorie_intake_calc(52.4,172.29,12,'F',0.06,'M')
	cut.height = 170.09
	cut.bodyfat = 0.16
	cut.age = 55
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'

def test_case_1():
	cut = calorie_intake_calc(60.1,153.99,16,'M',0.23,'L')
	cut.height = 215.05
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 49
	cut.age = 44

def test_case_2():
	cut = calorie_intake_calc(81.21,190.54,42,'N',0.2,'V')
	cut.bodyfat = 0.23
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(111.39,200.23,56,'F',0.26,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.age = 46

