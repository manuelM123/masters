from cut import *

def test_case_0():
	cut = calorie_intake_calc(130.66,146.32,18,'N',0.32,'M')
	cut.amount_exercise = 'M'
	cut.age = 66
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(37.98,144.17,32,'F',0.39,'S')
	cut.bodyfat = 0.28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 207.11
	cut.bodyfat = 0.46

def test_case_3():
	cut = calorie_intake_calc(127.8,158.1,78,'F',0.51,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 21
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(142.31,201.11,41,'M',0.07,'S')
	cut.age = 14
	cut.amount_exercise = 'V'
	cut.weight = 41.79
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'

def test_case_5():
	cut = calorie_intake_calc(155.82,216.84,85,'M',0.25,'E')
	cut.age = 46
	cut.weight = 40.08
	cut.bodyfat = 0.67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

