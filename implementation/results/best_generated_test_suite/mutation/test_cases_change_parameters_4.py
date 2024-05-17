from cut import *

def test_case_0():
	cut = calorie_intake_calc(65.36,149.39,71,'F',-0.17,'S')
	cut.bodyfat = 0.05
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 174.39
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.height = 216.11
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(116.51,156.26,7,'M',-0.36,'S')
	cut.bodyfat = 0.7
	cut.gender = 'N'
	cut.height = 185.44
	cut.bodyfat = 0.34
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 212.5
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 171.12

def test_case_2():
	cut = calorie_intake_calc(73.44,172.23,19,'N',0.47,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.69
	cut.weight = 80.92

