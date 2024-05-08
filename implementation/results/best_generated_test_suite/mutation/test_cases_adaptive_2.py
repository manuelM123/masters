from cut import *

def test_case_0():
	cut = calorie_intake_calc(122.5,218.99,7,'M',0.55,'M')
	cut.bodyfat = 0.53
	cut.height = 160.79
	cut.age = 49
	cut.height = 167.96
	cut.amount_exercise = 'M'
	cut.gender = 'M'
	cut.weight = 194.54

def test_case_1():
	cut = calorie_intake_calc(124.36,213.27,62,'F',-0.11,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 13
	cut.bodyfat = -0.25
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.37

def test_case_2():
	cut = calorie_intake_calc(108.9,213.31,49,'M',-0.45,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.height = 160.13
	result_determine_calorie_intake = cut.determine_calorie_intake()

