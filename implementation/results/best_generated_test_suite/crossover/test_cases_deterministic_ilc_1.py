from cut import *

def test_case_0():
	cut = calorie_intake_calc(64.06,166.34,48,'M',0.01,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.age = 38

def test_case_1():
	cut = calorie_intake_calc(64.91,168.61,76,'F',0.04,'E')
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 63.2
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(185.24,189.73,36,'N',0.28,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.1
	cut.bodyfat = 0.14
	cut.height = 201.7

