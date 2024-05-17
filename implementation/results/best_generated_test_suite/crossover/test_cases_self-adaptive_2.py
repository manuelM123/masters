from cut import *

def test_case_0():
	cut = calorie_intake_calc(131.52,187.08,36,'F',0.59,'M')
	cut.weight = 132.95
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 217.46
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	cut.gender = 'F'
	cut.height = 142.74
	cut.height = 153.04

def test_case_1():
	cut = calorie_intake_calc(63.95,163.46,43,'M',-0.08,'L')
	cut.height = 191.9
	cut.bodyfat = 0.39
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 60.44
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(116.97,147.31,6,'M',-0.23,'M')
	cut.height = 156.92
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 216.72
	cut.height = 221.66
	cut.bodyfat = 0.09
	cut.weight = 169.78
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.17

def test_case_3():
	cut = calorie_intake_calc(142.69,199.84,73,'N',0.45,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 7
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.age = 69
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(190.61,167.39,61,'M',-0.13,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 136.57
	cut.gender = 'F'
	cut.height = 186.61
	cut.age = 13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 48
	cut.weight = 134.83

def test_case_5():
	cut = calorie_intake_calc(153.61,201.03,67,'M',0.14,'M')
	cut.height = 162.49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 71
	cut.bodyfat = -0.44
	cut.weight = 180.11
	cut.amount_exercise = 'M'
	cut.age = 64

def test_case_6():
	cut = calorie_intake_calc(193.12,220.49,78,'F',0.63,'L')
	cut.age = 31
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(64.48,182.33,9,'N',0.67,'N')
	cut.age = 80
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

