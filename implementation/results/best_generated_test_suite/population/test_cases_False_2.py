from cut import *

def test_case_0():
	cut = calorie_intake_calc(87.53,150.17,65,'F',0.11,'M')
	cut.weight = 207.01
	cut.gender = 'F'
	cut.gender = 'N'
	cut.bodyfat = 0.02
	cut.height = 145.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.22
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(191.39,184.0,44,'M',0.16,'M')
	cut.height = 181.81
	cut.bodyfat = 0.24
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 164.63
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.height = 169.54

def test_case_2():
	cut = calorie_intake_calc(207.99,200.88,13,'F',0.18,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 208.17
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(45.67,149.66,32,'M',0.24,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 149.67
	cut.height = 151.77
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 178.51
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.0

def test_case_4():
	cut = calorie_intake_calc(187.86,209.36,28,'M',0.12,'S')
	cut.weight = 102.41
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.height = 163.68
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 62

