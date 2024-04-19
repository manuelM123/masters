from cut import *

def test_case_0():
	cut = calorie_intake_calc(153.06,177.99,64,'M',0.03,'V')
	cut.weight = 173.52
	cut.height = 180.19
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
	cut = calorie_intake_calc(199.22,151.77,25,'N',0.04,'S')
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(75.47,194.36,49,'M',0.17,'N')
	cut.amount_exercise = 'V'
	cut.weight = 93.67
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 79.06

def test_case_5():
	cut = calorie_intake_calc(128.49,142.57,68,'N',0.26,'L')
	cut.age = 36

def test_case_6():
	cut = calorie_intake_calc(198.63,186.6,27,'F',0.1,'E')
	cut.bodyfat = 0.07
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.age = 75

def test_case_7():
	cut = calorie_intake_calc(196.12,182.68,55,'M',0.15,'V')

def test_case_8():
	cut = calorie_intake_calc(80.28,145.87,55,'N',0.07,'M')
	cut.age = 55
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.age = 74
	cut.age = 45
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 44

def test_case_9():
	cut = calorie_intake_calc(202.66,145.41,43,'F',0.18,'M')
	cut.bodyfat = 0.2
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 20
	cut.amount_exercise = 'N'
	cut.gender = 'M'

