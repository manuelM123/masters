from cut import *

def test_case_0():
	cut = calorie_intake_calc(200.55,187.4,36,'N',0.52,'V')

def test_case_1():
	cut = calorie_intake_calc(139.41,182.35,11,'F',-0.34,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 205.41
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(130.25,176.75,14,'M',-0.38,'E')
	cut.height = 217.73
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 8

def test_case_3():
	cut = calorie_intake_calc(173.75,158.18,31,'M',-0.4,'N')
	cut.gender = 'M'
	cut.height = 176.68
	cut.bodyfat = -0.48
	cut.age = 75

