from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.48,156.24,35,'M',-0.48,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 50.0
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.66
	cut.weight = 38.82
	cut.height = 214.18

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(159.91,179.66,65,'M',0.77,'E')
	cut.weight = 131.69
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(64.52,139.7,5,'F',0.64,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(144.42,224.32,18,'M',0.04,'N')
	cut.age = 71

def test_case_5():
	cut = calorie_intake_calc(149.06,155.09,45,'N',-0.26,'S')
	cut.height = 180.11
	cut.gender = 'F'
	cut.height = 180.23
	cut.amount_exercise = 'S'
	cut.age = 83
	cut.bodyfat = 0.4
	cut.age = 72

def test_case_6():
	cut = calorie_intake_calc(126.46,139.76,11,'N',0.17,'M')
	cut.gender = 'F'
	cut.age = 83

