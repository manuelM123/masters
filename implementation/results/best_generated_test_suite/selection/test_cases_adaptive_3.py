from cut import *

def test_case_0():
	cut = calorie_intake_calc(80.25,157.68,53,'F',0.1,'M')
	cut.bodyfat = 0.2
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 152.14
	cut.age = 80
	cut.bodyfat = 0.02
	cut.amount_exercise = 'M'
	cut.height = 213.09
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(49.66,156.64,14,'N',0.27,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.15
	cut.amount_exercise = 'N'
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.06
	cut.height = 144.43
	cut.height = 192.24
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(184.52,150.11,38,'M',0.18,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 200.48
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

