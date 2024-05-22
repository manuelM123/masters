from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.48,156.24,35,'M',-0.48,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 50.0
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.66
	cut.weight = 38.82
	cut.height = 214.18

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(109.35,137.29,44,'M',0.2,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 146.45
	cut.gender = 'N'
	cut.weight = 194.69
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.01
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(70.12,210.54,57,'N',-0.36,'M')
	cut.bodyfat = 0.57

