from cut import *

def test_case_0():
	cut = calorie_intake_calc(68.07,206.4,77,'M',0.24,'V')
	cut.bodyfat = 0.14
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 44.61

def test_case_1():
	cut = calorie_intake_calc(103.87,144.47,76,'M',0.03,'S')
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.11
	cut.height = 199.6
	cut.gender = 'N'
	cut.age = 35

def test_case_2():
	cut = calorie_intake_calc(64.32,145.91,75,'F',0.04,'S')
	cut.bodyfat = 0.14
	cut.height = 165.83
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(210.1,201.57,78,'N',0.03,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.bodyfat = 0.28

def test_case_4():
	cut = calorie_intake_calc(147.2,144.73,48,'M',0.02,'N')
	cut.height = 180.94
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 59.31
	cut.bodyfat = 0.08
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(63.33,206.97,38,'M',0.15,'S')
	cut.gender = 'M'
	cut.age = 23
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	cut.weight = 124.42

def test_case_6():
	cut = calorie_intake_calc(120.74,212.98,75,'F',0.04,'E')
	cut.age = 34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 181.48
	cut.amount_exercise = 'M'
	cut.weight = 161.82
	cut.gender = 'F'
	cut.bodyfat = 0.21
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 198.38

def test_case_7():
	cut = calorie_intake_calc(208.59,159.47,36,'F',0.21,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 177.17
	cut.weight = 50.49
	cut.bodyfat = 0.29
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

