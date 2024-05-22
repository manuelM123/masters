from cut import *

def test_case_0():
	cut = calorie_intake_calc(205.97,164.05,10,'M',0.74,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 61

def test_case_1():
	cut = calorie_intake_calc(49.31,164.88,83,'M',0.66,'L')
	cut.amount_exercise = 'S'

def test_case_2():
	cut = calorie_intake_calc(127.43,180.36,40,'M',0.15,'E')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.48
	cut.gender = 'F'
	cut.height = 136.41

def test_case_3():
	cut = calorie_intake_calc(55.36,197.75,18,'F',0.07,'E')
	cut.amount_exercise = 'V'
	cut.weight = 113.16
	cut.bodyfat = 0.16
	cut.weight = 77.78
	cut.age = 13
	cut.weight = 40.48
	cut.age = 43
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.39

def test_case_4():
	cut = calorie_intake_calc(205.38,152.77,24,'M',0.22,'L')
	cut.height = 199.27
	cut.gender = 'F'
	cut.gender = 'F'
	cut.bodyfat = -0.47
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.02
	cut.bodyfat = -0.47
	cut.bodyfat = 0.32
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(205.12,217.45,67,'N',0.46,'V')
	cut.gender = 'F'
	cut.weight = 203.24
	cut.gender = 'F'
	cut.gender = 'F'
	cut.height = 156.82

