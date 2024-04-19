from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.77,192.23,10,'F',0.21,'S')
	cut.height = 146.4
	cut.gender = 'M'
	cut.height = 211.07
	result_determine_calorie_intake = cut.determine_calorie_intake()

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
	cut = calorie_intake_calc(105.49,163.83,56,'F',0.08,'S')
	cut.weight = 152.23
	cut.weight = 61.12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 118.43
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	cut.bodyfat = 0.17
	cut.height = 182.24
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 214.54

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
	cut.gender = 'M'

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
	cut = calorie_intake_calc(48.72,192.29,31,'F',0.18,'E')
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 115.59
	cut.age = 61
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 158.44
	cut.amount_exercise = 'L'
	cut.weight = 104.91

