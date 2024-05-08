from cut import *

def test_case_0():
	cut = calorie_intake_calc(86.58,199.82,61,'M',-0.25,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.46
	cut.height = 139.19
	cut.height = 151.46
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(209.89,186.0,80,'N',0.34,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.14
	cut.bodyfat = 0.27
	cut.age = 68
	cut.age = 61
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(142.79,145.85,10,'F',0.36,'S')
	cut.height = 149.61
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(195.65,209.41,39,'N',0.74,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(58.97,212.46,38,'N',-0.36,'E')

def test_case_5():
	cut = calorie_intake_calc(90.94,216.18,53,'N',0.8,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 155.8
	cut.amount_exercise = 'L'
	cut.weight = 125.56

def test_case_6():
	cut = calorie_intake_calc(100.49,176.27,26,'F',0.61,'L')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(151.86,146.25,66,'N',-0.49,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(100.55,145.0,5,'N',0.7,'E')

def test_case_9():
	cut = calorie_intake_calc(143.13,208.94,55,'N',0.36,'V')
	cut.weight = 148.52
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 15
	cut.gender = 'N'
	cut.age = 60
	cut.bodyfat = 0.11
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.07
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

