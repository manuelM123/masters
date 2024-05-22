from cut import *

def test_case_0():
	cut = calorie_intake_calc(107.17,210.47,23,'N',-0.33,'S')
	cut.age = 28
	cut.height = 221.16
	cut.age = 39
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.height = 156.32

def test_case_1():
	cut = calorie_intake_calc(67.08,151.41,29,'F',0.24,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 220.53
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.26

def test_case_2():
	cut = calorie_intake_calc(109.98,140.78,34,'M',-0.08,'L')
	cut.gender = 'F'
	cut.age = 58
	cut.age = 20
	cut.weight = 58.3
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 85.37
	cut.height = 177.97
	cut.age = 51

def test_case_3():
	cut = calorie_intake_calc(171.76,190.44,33,'M',-0.31,'L')
	cut.weight = 37.32
	cut.weight = 198.65
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 188.02
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(84.52,161.72,44,'N',-0.08,'E')
	cut.amount_exercise = 'L'
	cut.weight = 76.26
	cut.age = 77
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(181.48,198.07,13,'N',0.11,'M')

def test_case_6():
	cut = calorie_intake_calc(203.08,222.45,67,'F',0.09,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 39.92
	cut.height = 182.72
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(74.96,218.0,45,'M',-0.28,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.weight = 84.69
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 53
	cut.height = 143.43

def test_case_8():
	cut = calorie_intake_calc(143.21,154.49,76,'F',0.25,'M')
	cut.bodyfat = -0.08
	cut.amount_exercise = 'L'
	cut.age = 27
	cut.bodyfat = 0.08
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 140.14
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.53

