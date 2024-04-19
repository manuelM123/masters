from cut import *

def test_case_0():
	cut = calorie_intake_calc(131.71,185.16,70,'F',0.09,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'

def test_case_1():
	cut = calorie_intake_calc(152.19,190.79,80,'F',0.12,'N')
	cut.bodyfat = 0.13
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.03
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(64.32,145.91,75,'F',0.04,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 165.83
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(195.8,216.29,31,'M',0.15,'N')
	cut.age = 44
	cut.weight = 164.99
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(103.62,173.19,38,'F',0.24,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 80
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.08

def test_case_5():
	cut = calorie_intake_calc(75.18,151.63,38,'N',0.01,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(81.79,196.07,41,'F',0.11,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 164.94
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_7():
	cut = calorie_intake_calc(81.94,187.86,55,'M',0.18,'N')
	cut.bodyfat = 0.08
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 79
	cut.height = 192.32
	cut.bodyfat = 0.13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 211.37

def test_case_8():
	cut = calorie_intake_calc(198.54,195.26,62,'F',0.02,'V')
	cut.age = 28
	cut.height = 214.69
	cut.weight = 63.09
	cut.age = 16

def test_case_9():
	cut = calorie_intake_calc(132.74,148.95,25,'M',0.16,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 196.57
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 181.88
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 62

