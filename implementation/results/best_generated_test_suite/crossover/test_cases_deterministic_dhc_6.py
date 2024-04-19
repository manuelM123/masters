from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.77,192.23,10,'F',0.21,'S')
	cut.height = 146.4
	cut.gender = 'M'
	cut.height = 211.07
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(97.07,169.64,44,'F',0.02,'E')
	result_tdee_calculation = cut.tdee_calculation()

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
	cut = calorie_intake_calc(64.6,141.07,59,'M',0.22,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 73.67
	cut.height = 169.7
	cut.bodyfat = 0.23
	cut.age = 52
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.weight = 175.32
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(177.64,141.47,69,'N',0.1,'M')
	cut.age = 40
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 18

