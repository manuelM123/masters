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
	result_tdee_calculation = cut.tdee_calculation()

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
	cut = calorie_intake_calc(102.77,167.83,72,'M',0.13,'E')
	cut.bodyfat = 0.46
	cut.bodyfat = 0.62
	cut.height = 221.04
	cut.height = 185.51
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'

def test_case_6():
	cut = calorie_intake_calc(97.17,224.66,84,'M',-0.02,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.61
	cut.weight = 41.86
	cut.height = 214.69
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(59.46,195.93,66,'F',-0.37,'E')
	cut.age = 22
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 50.79
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 72

