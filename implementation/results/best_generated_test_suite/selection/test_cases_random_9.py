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
	cut = calorie_intake_calc(167.72,173.6,8,'F',0.48,'M')
	cut.gender = 'F'
	cut.age = 76
	cut.height = 212.97
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(142.79,145.85,10,'F',0.36,'S')
	cut.height = 149.61
	cut.bodyfat = 0.26
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(183.45,186.26,43,'F',0.79,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10
	cut.height = 138.46
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 164.51

def test_case_4():
	cut = calorie_intake_calc(96.63,185.74,33,'F',0.5,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 160.69
	cut.gender = 'N'
	cut.height = 175.37
	cut.weight = 162.31
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(90.94,216.18,53,'N',0.8,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 155.8
	cut.amount_exercise = 'L'
	cut.weight = 125.56

def test_case_6():
	cut = calorie_intake_calc(74.64,164.54,15,'F',-0.18,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.gender = 'F'
	cut.bodyfat = -0.01
	cut.amount_exercise = 'N'
	cut.height = 159.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

