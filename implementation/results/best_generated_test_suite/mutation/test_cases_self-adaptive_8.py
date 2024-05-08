from cut import *

def test_case_0():
	cut = calorie_intake_calc(36.69,168.33,53,'N',0.18,'V')

def test_case_1():
	cut = calorie_intake_calc(98.86,204.45,60,'N',-0.47,'L')
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.28
	cut.bodyfat = 0.63
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.gender = 'M'
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(48.63,194.82,14,'F',0.17,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 27
	cut.age = 85

def test_case_3():
	cut = calorie_intake_calc(187.34,213.05,82,'N',0.37,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.47
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

