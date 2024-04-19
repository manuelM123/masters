from cut import *

def test_case_0():
	cut = calorie_intake_calc(153.06,177.99,64,'M',0.03,'V')
	cut.weight = 173.52
	cut.bodyfat = 0.24
	cut.weight = 139.25
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 157.37
	cut.weight = 189.0
	cut.age = 16
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(122.21,205.6,69,'M',0.12,'S')
	cut.height = 156.76
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 44

def test_case_2():
	cut = calorie_intake_calc(58.13,177.86,39,'F',0.27,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 81.03
	cut.height = 193.5
	cut.age = 34
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.1

def test_case_3():
	cut = calorie_intake_calc(63.37,158.28,72,'N',0.01,'S')
	cut.height = 201.19
	cut.amount_exercise = 'N'
	cut.height = 206.34
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.amount_exercise = 'S'

def test_case_4():
	cut = calorie_intake_calc(75.47,194.36,49,'M',0.17,'N')
	cut.amount_exercise = 'V'
	cut.weight = 93.67
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 79.06

def test_case_5():
	cut = calorie_intake_calc(181.9,216.51,62,'M',0.17,'N')
	cut.weight = 170.4
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(125.49,144.61,23,'F',0.18,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 152.9

def test_case_7():
	cut = calorie_intake_calc(196.12,182.68,55,'M',0.15,'V')

