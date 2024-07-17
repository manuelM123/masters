from cut import *

def test_case_0():
	cut = calorie_intake_calc(52.53,152.58,40,'F',0.09,'L')
	cut.weight = 35.8

def test_case_1():
	cut = calorie_intake_calc(111.42,170.3,69,'F',-0.03,'S')

def test_case_2():
	cut = calorie_intake_calc(206.57,148.11,13,'N',-0.14,'E')
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 13

def test_case_3():
	cut = calorie_intake_calc(204.59,170.19,12,'F',0.13,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

