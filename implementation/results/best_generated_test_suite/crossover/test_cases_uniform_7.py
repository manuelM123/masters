from cut import *

def test_case_0():
	cut = calorie_intake_calc(181.51,188.47,13,'F',0.52,'N')

def test_case_1():
	cut = calorie_intake_calc(157.04,162.52,47,'F',-0.26,'E')
	cut.age = 13
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(180.9,185.99,45,'M',0.47,'S')
	cut.age = 31
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.32
	cut.age = 52
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(96.24,175.33,50,'M',0.63,'L')
	cut.height = 183.3
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(66.83,145.86,7,'M',-0.5,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'

def test_case_5():
	cut = calorie_intake_calc(93.52,172.9,52,'N',-0.17,'V')
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.age = 57

def test_case_6():
	cut = calorie_intake_calc(132.55,219.53,28,'M',0.15,'L')
	cut.weight = 72.02
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

