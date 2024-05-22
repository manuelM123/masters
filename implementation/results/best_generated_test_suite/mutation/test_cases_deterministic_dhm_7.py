from cut import *

def test_case_0():
	cut = calorie_intake_calc(56.78,198.54,55,'F',0.3,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(42.76,157.24,54,'N',0.79,'E')
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.gender = 'N'
	cut.age = 32

def test_case_2():
	cut = calorie_intake_calc(42.76,157.24,54,'N',0.79,'E')
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.gender = 'N'
	cut.age = 32

def test_case_3():
	cut = calorie_intake_calc(51.23,153.05,39,'M',-0.04,'L')
	cut.bodyfat = -0.17
	cut.age = 73
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 193.14
	cut.height = 167.79
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(173.73,197.76,15,'F',0.22,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 174.65
	cut.bodyfat = -0.13
	cut.gender = 'F'
	cut.age = 18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(181.19,215.62,66,'N',0.77,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(105.34,170.05,17,'F',0.31,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.08
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 122.84
	cut.amount_exercise = 'L'

def test_case_7():
	cut = calorie_intake_calc(171.31,162.11,45,'M',0.75,'N')
	cut.weight = 57.81
	cut.age = 53

