from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.87,182.94,71,'F',0.04,'V')
	cut.gender = 'F'
	cut.bodyfat = 0.29
	cut.weight = 157.69
	cut.bodyfat = 0.29
	cut.bodyfat = 0.1
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 204.71
	cut.weight = 192.42
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(169.85,140.41,38,'F',0.01,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.gender = 'F'
	cut.amount_exercise = 'M'

def test_case_2():
	cut = calorie_intake_calc(143.16,141.4,49,'M',0.3,'M')
	cut.bodyfat = 0.19
	cut.height = 147.69
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(117.17,188.39,56,'F',0.24,'E')
	cut.height = 166.84

def test_case_4():
	cut = calorie_intake_calc(97.22,196.15,22,'M',0.26,'L')
	cut.weight = 126.92
	cut.age = 64
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	cut.age = 29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.0
	cut.age = 42
	cut.age = 51

