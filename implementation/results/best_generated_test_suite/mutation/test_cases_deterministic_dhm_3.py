from cut import *

def test_case_0():
	cut = calorie_intake_calc(49.21,154.31,32,'N',0.02,'L')
	cut.height = 148.04
	cut.height = 146.0
	cut.weight = 184.63
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(97.2,162.89,75,'N',0.08,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 50.61
	cut.bodyfat = 0.16
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 79

def test_case_2():
	cut = calorie_intake_calc(97.64,145.17,15,'F',0.29,'N')
	cut.gender = 'F'
	cut.bodyfat = 0.17
	cut.bodyfat = 0.1

def test_case_3():
	cut = calorie_intake_calc(132.44,182.53,34,'M',0.27,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 173.76
	cut.age = 35
	cut.weight = 208.56
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.weight = 85.59
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(57.79,140.63,52,'F',0.02,'V')
	cut.gender = 'N'
	cut.age = 72
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 159.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 181.01
	cut.weight = 208.05
	cut.gender = 'N'

def test_case_5():
	cut = calorie_intake_calc(139.98,184.73,76,'M',0.13,'E')
	cut.height = 208.44
	cut.bodyfat = 0.16
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'S'

