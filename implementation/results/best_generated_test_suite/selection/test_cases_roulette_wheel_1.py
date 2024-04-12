from cut import *

def test_case_0():
	cut = calorie_intake_calc(151.97,160.35,69,'N',0.16,'E')
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.0
	cut.height = 170.16

def test_case_1():
	cut = calorie_intake_calc(209.73,163.39,40,'F',0.0,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 56
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.29
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(43.92,195.5,50,'N',0.19,'V')
	cut.age = 13
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'V'

def test_case_3():
	cut = calorie_intake_calc(163.37,198.22,76,'N',0.26,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	cut.gender = 'M'
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 153.31
	cut.bodyfat = 0.07
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(208.43,158.92,10,'M',0.02,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 147.46
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

