from cut import *

def test_case_0():
	cut = calorie_intake_calc(177.72,204.0,69,'M',0.23,'V')
	cut.weight = 102.72
	cut.age = 25
	cut.amount_exercise = 'V'
	cut.height = 201.48
	cut.weight = 149.35
	cut.age = 69
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 141.4

def test_case_1():
	cut = calorie_intake_calc(43.63,141.66,33,'M',0.05,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.25
	cut.age = 13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(158.77,213.9,73,'F',0.2,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(137.21,196.69,16,'M',0.01,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 84.34
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 147.42

def test_case_4():
	cut = calorie_intake_calc(209.9,163.67,49,'N',0.12,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.0
	result_determine_calorie_intake = cut.determine_calorie_intake()

