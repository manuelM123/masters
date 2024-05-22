from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.48,156.24,35,'M',-0.48,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 50.0
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.weight = 38.82
	cut.height = 214.18

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(120.84,162.4,5,'N',0.0,'M')
	cut.amount_exercise = 'V'
	cut.height = 224.75

def test_case_3():
	cut = calorie_intake_calc(71.07,187.96,65,'N',-0.22,'E')
	cut.amount_exercise = 'V'
	cut.bodyfat = -0.48
	cut.weight = 43.94
	cut.height = 136.53

