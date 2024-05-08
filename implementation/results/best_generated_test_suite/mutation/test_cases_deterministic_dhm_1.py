from cut import *

def test_case_0():
	cut = calorie_intake_calc(172.06,141.55,42,'M',-0.38,'M')
	cut.height = 191.62
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(139.24,213.07,83,'N',0.41,'V')
	cut.gender = 'F'
	cut.age = 50
	cut.age = 42
	cut.amount_exercise = 'S'

def test_case_2():
	cut = calorie_intake_calc(177.03,165.32,73,'N',0.68,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.amount_exercise = 'V'
	cut.gender = 'N'
	cut.gender = 'F'
	cut.age = 12

def test_case_3():
	cut = calorie_intake_calc(87.85,169.56,33,'N',-0.23,'N')
	cut.age = 16
	cut.gender = 'F'
	cut.height = 137.94

def test_case_4():
	cut = calorie_intake_calc(75.55,211.49,29,'N',-0.09,'S')

def test_case_5():
	cut = calorie_intake_calc(132.03,179.11,44,'F',0.29,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 218.92
	cut.height = 211.41
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	cut.weight = 188.22

def test_case_6():
	cut = calorie_intake_calc(145.84,138.32,39,'M',-0.22,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.27
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.13

