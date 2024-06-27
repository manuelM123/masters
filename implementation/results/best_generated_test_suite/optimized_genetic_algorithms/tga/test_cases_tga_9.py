from cut import *

def test_case_0():
	cut = calorie_intake_calc(110.01,215.78,76,'M',-0.18,'L')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(103.46,164.4,20,'F',-0.36,'E')
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(35.57,197.94,24,'N',0.47,'L')
	cut.height = 184.59
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(121.71,182.98,74,'M',0.15,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.15
	cut.age = 44

