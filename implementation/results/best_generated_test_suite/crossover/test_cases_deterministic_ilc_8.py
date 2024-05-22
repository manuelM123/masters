from cut import *

def test_case_0():
	cut = calorie_intake_calc(128.09,181.9,18,'M',-0.17,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(103.8,224.33,22,'N',-0.38,'V')
	cut.bodyfat = 0.41
	cut.height = 201.21

def test_case_2():
	cut = calorie_intake_calc(118.28,151.18,49,'M',-0.09,'V')
	cut.bodyfat = -0.38

def test_case_3():
	cut = calorie_intake_calc(136.19,151.73,28,'N',0.77,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.23
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(49.81,178.64,37,'M',0.5,'L')
	cut.age = 74
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.weight = 116.6
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 187.44
	cut.height = 205.05
	cut.gender = 'N'

