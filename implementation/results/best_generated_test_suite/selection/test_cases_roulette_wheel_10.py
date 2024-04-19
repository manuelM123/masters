from cut import *

def test_case_0():
	cut = calorie_intake_calc(64.49,166.1,79,'F',0.22,'M')
	cut.bodyfat = 0.14
	cut.age = 29
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 44.61

def test_case_1():
	cut = calorie_intake_calc(103.87,144.47,76,'M',0.03,'S')
	cut.amount_exercise = 'L'
	cut.gender = 'N'
	cut.weight = 110.1
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 103.92
	cut.height = 199.6
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(48.11,147.21,81,'M',0.19,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.0
	cut.amount_exercise = 'N'

def test_case_3():
	cut = calorie_intake_calc(159.38,187.09,66,'F',0.24,'N')
	cut.weight = 146.72

def test_case_4():
	cut = calorie_intake_calc(147.2,144.73,48,'M',0.02,'N')
	cut.amount_exercise = 'V'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 59.31
	cut.bodyfat = 0.08
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(63.33,206.97,38,'M',0.15,'S')
	cut.weight = 186.31
	cut.age = 23
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	cut.weight = 124.42

def test_case_6():
	cut = calorie_intake_calc(195.85,168.59,50,'M',0.16,'E')
	cut.age = 34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 181.48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 161.82
	cut.gender = 'F'
	cut.bodyfat = 0.21
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 198.38

def test_case_7():
	cut = calorie_intake_calc(208.59,159.47,36,'F',0.21,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.28
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.29
	cut.weight = 122.68
	cut.weight = 143.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(185.67,151.44,43,'F',0.11,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 147.02
	cut.gender = 'F'

