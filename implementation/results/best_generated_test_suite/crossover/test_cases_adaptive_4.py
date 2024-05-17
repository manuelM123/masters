from cut import *

def test_case_0():
	cut = calorie_intake_calc(133.44,188.03,40,'M',0.02,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(82.0,168.49,52,'F',-0.45,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(144.78,217.97,18,'M',0.46,'V')
	cut.bodyfat = 0.05
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.34
	cut.amount_exercise = 'E'

def test_case_3():
	cut = calorie_intake_calc(199.2,156.31,76,'N',-0.05,'L')

