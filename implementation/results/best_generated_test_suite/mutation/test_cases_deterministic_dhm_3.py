from cut import *

def test_case_0():
	cut = calorie_intake_calc(173.43,145.56,63,'M',0.24,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 162.11

def test_case_1():
	cut = calorie_intake_calc(39.86,193.18,70,'N',0.33,'M')
	cut.age = 59
	cut.height = 218.27
	cut.bodyfat = -0.25
	cut.weight = 75.44
	cut.height = 178.32
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(197.39,157.98,27,'F',0.3,'M')
	cut.bodyfat = 0.78
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(67.07,142.47,51,'M',-0.07,'E')
	cut.bodyfat = -0.49
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 29
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(150.76,162.95,52,'N',0.79,'S')
	cut.bodyfat = 0.03
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

