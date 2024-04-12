from cut import *

def test_case_0():
	cut = calorie_intake_calc(203.51,142.18,77,'F',0.17,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 81
	cut.height = 161.15
	cut.height = 219.8
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(126.26,158.67,68,'N',0.26,'E')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(110.19,142.83,13,'N',0.27,'E')
	cut.age = 34
	cut.age = 41
	cut.weight = 147.37
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(177.9,161.89,12,'M',0.21,'N')
	cut.amount_exercise = 'S'
	cut.weight = 110.92
	cut.age = 24
	cut.age = 73
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'N'
	cut.gender = 'F'
	cut.amount_exercise = 'V'

def test_case_4():
	cut = calorie_intake_calc(134.9,156.1,35,'M',0.19,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 159.78
	cut.height = 216.08
	cut.bodyfat = 0.15
	cut.amount_exercise = 'M'
	cut.height = 145.8

