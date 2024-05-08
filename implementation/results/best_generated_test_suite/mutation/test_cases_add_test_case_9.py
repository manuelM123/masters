from cut import *

def test_case_0():
	cut = calorie_intake_calc(124.69,220.25,28,'N',-0.31,'M')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(139.24,213.07,83,'N',0.41,'V')
	cut.gender = 'F'
	cut.age = 50
	cut.age = 42
	cut.amount_exercise = 'L'

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
	cut = calorie_intake_calc(61.9,166.99,34,'F',0.28,'M')
	cut.age = 16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

