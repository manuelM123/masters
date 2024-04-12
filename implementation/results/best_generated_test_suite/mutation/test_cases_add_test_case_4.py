from cut import *

def test_case_0():
	cut = calorie_intake_calc(157.62,145.88,47,'N',0.1,'L')
	cut.bodyfat = 0.18
	cut.gender = 'N'
	cut.bodyfat = 0.0
	cut.weight = 78.05

def test_case_1():
	cut = calorie_intake_calc(106.78,213.63,21,'F',0.03,'E')
	cut.age = 75
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'M'
	cut.height = 147.4
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 27
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(193.52,174.73,11,'M',0.06,'E')
	cut.age = 29

def test_case_3():
	cut = calorie_intake_calc(131.88,219.78,16,'F',0.16,'S')
	cut.height = 195.52
	cut.bodyfat = 0.13
	cut.age = 60

def test_case_4():
	cut = calorie_intake_calc(171.4,209.23,21,'M',0.19,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.gender = 'N'
	cut.bodyfat = 0.07
	cut.bodyfat = 0.23
	cut.bodyfat = 0.08

