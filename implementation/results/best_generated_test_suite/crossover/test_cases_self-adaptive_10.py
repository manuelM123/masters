from cut import *

def test_case_0():
	cut = calorie_intake_calc(145.56,136.42,9,'M',0.09,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 199.15
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(192.76,202.07,18,'M',-0.4,'S')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.31
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	cut.height = 195.39
	cut.gender = 'N'
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(153.49,167.77,17,'M',0.27,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 61
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

