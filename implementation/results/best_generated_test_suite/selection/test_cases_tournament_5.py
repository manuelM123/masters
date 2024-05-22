from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.48,156.24,35,'M',-0.48,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 50.0
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 145.69
	cut.weight = 38.82
	cut.height = 214.18

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(132.04,195.15,37,'F',-0.01,'E')
	cut.weight = 131.69
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(175.18,158.27,47,'F',0.13,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 81
	cut.height = 187.07
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_4():
	cut = calorie_intake_calc(112.12,153.12,40,'M',-0.21,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.06
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 168.32
	cut.height = 156.29

def test_case_5():
	cut = calorie_intake_calc(171.95,141.93,77,'N',0.67,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.gender = 'N'
	cut.gender = 'F'

