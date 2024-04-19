from cut import *

def test_case_0():
	cut = calorie_intake_calc(57.07,196.67,28,'F',0.26,'V')
	cut.gender = 'M'
	cut.weight = 190.61
	cut.bodyfat = 0.16
	cut.height = 207.13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 22
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(187.27,202.81,81,'N',0.25,'M')
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	cut.height = 150.78
	cut.gender = 'M'
	cut.bodyfat = 0.18
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.age = 67
	cut.bodyfat = 0.27

def test_case_2():
	cut = calorie_intake_calc(113.18,159.43,10,'F',0.28,'L')
	cut.bodyfat = 0.27
	cut.amount_exercise = 'L'
	cut.weight = 45.55

def test_case_3():
	cut = calorie_intake_calc(151.81,179.36,49,'N',0.22,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.height = 175.92
	cut.height = 165.92

def test_case_4():
	cut = calorie_intake_calc(191.62,205.62,16,'M',0.23,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 62.19
	cut.gender = 'N'

