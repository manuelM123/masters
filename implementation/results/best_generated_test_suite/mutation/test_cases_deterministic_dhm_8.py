from cut import *

def test_case_0():
	cut = calorie_intake_calc(72.89,162.14,44,'F',0.27,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(58.33,206.6,28,'N',0.22,'N')
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 52
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 160.08
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(193.88,145.68,73,'N',0.14,'M')
	cut.bodyfat = 0.07
	cut.age = 59
	cut.weight = 165.67
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(130.68,199.89,33,'M',0.23,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 28
	cut.height = 145.35
	cut.gender = 'M'
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(167.26,150.98,49,'M',0.0,'N')
	cut.weight = 189.79
	cut.age = 18
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.1

def test_case_5():
	cut = calorie_intake_calc(168.65,193.09,70,'N',0.09,'V')
	cut.weight = 205.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	cut.weight = 199.61
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 67.6
	cut.height = 181.4

