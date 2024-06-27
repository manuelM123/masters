from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.56,212.61,14,'M',-0.43,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 141.42

def test_case_1():
	cut = calorie_intake_calc(94.35,182.65,47,'F',-0.25,'E')
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 61.62

def test_case_2():
	cut = calorie_intake_calc(135.23,166.47,37,'M',-0.12,'N')
	cut.height = 139.01
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 210.87
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(152.16,160.22,44,'M',-0.35,'M')
	result_tdee_calculation = cut.tdee_calculation()

