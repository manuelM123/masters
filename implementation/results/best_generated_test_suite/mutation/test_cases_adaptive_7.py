from cut import *

def test_case_0():
	cut = calorie_intake_calc(38.83,141.0,69,'N',-0.14,'V')
	cut.gender = 'F'
	cut.amount_exercise = 'L'
	cut.weight = 66.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(115.1,141.86,75,'F',-0.28,'E')
	cut.weight = 54.55
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 209.58
	cut.age = 16
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(167.07,196.84,31,'M',0.33,'L')
	cut.height = 143.92

