from cut import *

def test_case_0():
	cut = calorie_intake_calc(194.68,176.26,69,'M',0.06,'E')
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 53

def test_case_1():
	cut = calorie_intake_calc(164.69,158.47,77,'M',0.03,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 178.12

def test_case_2():
	cut = calorie_intake_calc(138.31,213.95,47,'M',-0.09,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(79.41,222.1,66,'N',0.1,'E')
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

