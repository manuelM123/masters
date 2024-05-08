from cut import *

def test_case_0():
	cut = calorie_intake_calc(94.64,182.91,44,'N',-0.31,'L')
	cut.gender = 'F'
	cut.height = 205.66
	cut.gender = 'M'
	cut.bodyfat = -0.46
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.height = 170.06

def test_case_1():
	cut = calorie_intake_calc(102.95,167.33,37,'F',-0.38,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(78.33,202.77,77,'F',0.37,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(167.58,224.29,24,'N',0.12,'N')
	cut.weight = 55.77
	cut.weight = 133.9
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 56
	cut.age = 79
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(58.58,219.78,58,'M',-0.15,'E')

def test_case_5():
	cut = calorie_intake_calc(132.82,154.86,15,'N',0.55,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'

def test_case_6():
	cut = calorie_intake_calc(55.43,214.41,34,'M',-0.25,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 197.2
	cut.bodyfat = 0.06

