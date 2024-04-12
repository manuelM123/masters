from cut import *

def test_case_0():
	cut = calorie_intake_calc(40.64,212.56,62,'M',0.25,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(139.43,153.51,54,'M',0.05,'E')

def test_case_2():
	cut = calorie_intake_calc(111.46,174.35,77,'M',0.23,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 40
	cut.height = 155.73
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(70.94,164.63,26,'F',0.25,'S')
	cut.weight = 133.23
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 202.63
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 60
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(161.66,161.46,30,'N',0.25,'L')

