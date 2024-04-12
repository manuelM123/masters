from cut import *

def test_case_0():
	cut = calorie_intake_calc(158.41,167.38,50,'F',0.18,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.age = 78

def test_case_1():
	cut = calorie_intake_calc(125.73,174.94,43,'M',0.1,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.16
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.height = 171.51
	cut.bodyfat = 0.08

def test_case_2():
	cut = calorie_intake_calc(133.88,182.58,73,'M',0.1,'L')
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 23
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 142.1
	cut.gender = 'F'
	cut.weight = 110.2
	cut.bodyfat = 0.29
	cut.bodyfat = 0.09

def test_case_3():
	cut = calorie_intake_calc(196.57,173.57,60,'F',0.23,'E')
	cut.bodyfat = 0.24
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'

