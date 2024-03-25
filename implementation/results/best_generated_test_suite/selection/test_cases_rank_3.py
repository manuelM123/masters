from cut import *

def test_case_0():
	cut = calorie_intake_calc(85.53,196.01,55,'N',0.09,'N')

def test_case_1():
	cut = calorie_intake_calc(103.81,160.9,20,'F',0.25,'N')
	cut.weight = 79.83
	cut.height = 192.74
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(94.39,185.62,49,'M',0.26,'E')
	cut.age = 74

def test_case_3():
	cut = calorie_intake_calc(170.18,178.42,36,'M',0.19,'N')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(55.13,185.93,68,'F',0.25,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.age = 20
	cut.height = 210.35

def test_case_5():
	cut = calorie_intake_calc(195.49,169.76,77,'F',0.05,'N')
	cut.age = 39
	cut.height = 140.01
	cut.weight = 166.69
	cut.amount_exercise = 'L'
	cut.weight = 54.95
	cut.age = 27
	cut.amount_exercise = 'L'
	cut.height = 156.35

def test_case_6():
	cut = calorie_intake_calc(109.61,219.53,78,'M',0.29,'S')
	cut.weight = 179.84
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 214.8
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 214.43
	cut.age = 50
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

