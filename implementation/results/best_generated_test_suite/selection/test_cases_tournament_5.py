from cut import *

def test_case_0():
	cut = calorie_intake_calc(196.17,204.11,49,'M',0.23,'V')
	cut.weight = 94.62
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 10
	cut.age = 75
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(78.29,179.24,16,'F',0.1,'N')
	cut.height = 181.56
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.24
	cut.bodyfat = 0.02
	cut.age = 27
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(83.86,208.49,60,'M',0.14,'S')
	cut.weight = 59.13

