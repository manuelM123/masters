from cut import *

def test_case_0():
	cut = calorie_intake_calc(160.95,205.56,50,'M',0.09,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(207.9,165.87,42,'F',0.18,'V')
	cut.gender = 'F'
	cut.age = 67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 52

def test_case_2():
	cut = calorie_intake_calc(162.9,156.37,63,'N',0.27,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.05
	cut.amount_exercise = 'N'
	cut.height = 178.86
	cut.bodyfat = 0.01
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 162.49

