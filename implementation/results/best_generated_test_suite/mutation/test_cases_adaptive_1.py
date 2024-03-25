from cut import *

def test_case_0():
	cut = calorie_intake_calc(41.41,170.92,47,'F',0.17,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(149.13,162.49,81,'F',0.11,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 193.53
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 188.53
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 68.53

def test_case_2():
	cut = calorie_intake_calc(61.74,204.97,37,'N',0.19,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 177.85
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(135.58,145.23,54,'F',0.14,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 118.57
	cut.gender = 'M'
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

