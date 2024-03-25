from cut import *

def test_case_0():
	cut = calorie_intake_calc(145.08,174.16,63,'N',0.2,'V')
	cut.age = 61
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 46

def test_case_1():
	cut = calorie_intake_calc(168.69,154.12,56,'M',0.21,'S')
	cut.height = 200.85
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 148.95
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.weight = 127.4
	cut.weight = 62.47

def test_case_2():
	cut = calorie_intake_calc(130.91,208.25,44,'N',0.25,'V')
	result_tdee_calculation = cut.tdee_calculation()

