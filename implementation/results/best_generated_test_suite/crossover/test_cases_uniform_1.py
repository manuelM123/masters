from cut import *

def test_case_0():
	cut = calorie_intake_calc(126.87,156.38,25,'F',0.09,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.age = 53
	cut.height = 212.34
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.29
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(107.6,146.98,81,'M',0.25,'V')
	cut.weight = 63.62
	cut.height = 176.74
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 58
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(103.84,157.81,47,'F',0.17,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 192.43
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'

def test_case_3():
	cut = calorie_intake_calc(137.88,176.4,51,'N',0.21,'V')
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.weight = 146.48
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.age = 12

def test_case_4():
	cut = calorie_intake_calc(196.67,196.07,16,'N',0.21,'E')
	cut.weight = 101.34
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 36

