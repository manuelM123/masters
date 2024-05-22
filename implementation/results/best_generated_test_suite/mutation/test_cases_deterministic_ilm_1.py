from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 194.75
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.08
	cut.age = 69
	cut.age = 22

def test_case_1():
	cut = calorie_intake_calc(148.96,199.29,27,'F',0.13,'S')
	cut.age = 9
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 95.8

def test_case_2():
	cut = calorie_intake_calc(71.87,178.85,36,'M',-0.33,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 162.77
	cut.height = 178.63
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 171.14
	cut.age = 15
	cut.height = 175.0
	cut.bodyfat = 0.19
	cut.age = 55

def test_case_3():
	cut = calorie_intake_calc(144.75,210.51,14,'F',0.1,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.41
	cut.weight = 178.08
	cut.height = 210.41
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.18
	cut.gender = 'M'
	cut.amount_exercise = 'V'

def test_case_4():
	cut = calorie_intake_calc(184.77,200.31,79,'M',-0.42,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.31
	result_determine_calorie_intake = cut.determine_calorie_intake()

