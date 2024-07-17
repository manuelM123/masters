from cut import *

def test_case_0():
	cut = calorie_intake_calc(106.79,206.94,31,'N',0.11,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 144.66

def test_case_1():
	cut = calorie_intake_calc(100.95,148.66,52,'M',-0.03,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10
	cut.age = 60
	cut.bodyfat = 0.32

def test_case_2():
	cut = calorie_intake_calc(45.35,167.99,44,'F',-0.24,'E')
	cut.height = 186.87
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

