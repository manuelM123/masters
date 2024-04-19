from cut import *

def test_case_0():
	cut = calorie_intake_calc(178.77,182.01,44,'M',0.02,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.23
	cut.height = 208.58
	cut.height = 145.86

def test_case_1():
	cut = calorie_intake_calc(198.96,208.52,31,'F',0.29,'M')
	cut.weight = 78.75
	cut.age = 34

def test_case_2():
	cut = calorie_intake_calc(177.0,173.03,21,'F',0.08,'L')
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.04

def test_case_3():
	cut = calorie_intake_calc(78.66,208.9,34,'F',0.27,'N')
	cut.height = 174.28

def test_case_4():
	cut = calorie_intake_calc(199.53,161.63,22,'F',0.29,'L')
	cut.weight = 51.27
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	cut.height = 174.79
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 192.06
	cut.height = 190.6
	cut.age = 33
	cut.weight = 125.64

def test_case_5():
	cut = calorie_intake_calc(164.6,147.25,64,'N',0.24,'S')
	cut.bodyfat = 0.26

def test_case_6():
	cut = calorie_intake_calc(70.58,156.97,20,'F',0.12,'E')
	cut.height = 196.09
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.height = 206.76
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(113.23,167.56,17,'M',0.21,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_8():
	cut = calorie_intake_calc(130.39,174.3,52,'F',0.07,'L')
	cut.weight = 134.74
	cut.weight = 131.78
	cut.height = 199.7

def test_case_9():
	cut = calorie_intake_calc(162.27,142.28,26,'N',0.01,'M')
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 187.41
	cut.amount_exercise = 'L'
	cut.height = 206.32
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 206.49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 199.19

