from cut import *

def test_case_0():
	cut = calorie_intake_calc(149.71,190.76,32,'N',0.02,'M')
	cut.height = 206.15
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	cut.gender = 'F'

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
	cut = calorie_intake_calc(204.48,220.43,80,'F',0.03,'E')
	cut.bodyfat = 0.27
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(194.72,168.24,45,'F',0.09,'E')
	cut.amount_exercise = 'S'
	cut.weight = 72.73
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.25
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 175.39

def test_case_4():
	cut = calorie_intake_calc(135.68,160.4,68,'M',0.06,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 61.54
	cut.age = 48

def test_case_5():
	cut = calorie_intake_calc(207.12,158.4,59,'M',0.23,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.12
	cut.bodyfat = 0.15

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
	cut.weight = 177.17
	cut.bodyfat = 0.29
	cut.weight = 122.68
	cut.weight = 143.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

