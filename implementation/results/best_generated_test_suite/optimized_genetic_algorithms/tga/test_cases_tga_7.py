from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.56,212.61,14,'M',-0.43,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.12
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(56.2,213.18,56,'M',0.08,'M')
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(95.24,214.41,82,'N',0.6,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 73.36
	cut.bodyfat = 0.17

def test_case_3():
	cut = calorie_intake_calc(37.04,217.57,54,'M',0.17,'S')

