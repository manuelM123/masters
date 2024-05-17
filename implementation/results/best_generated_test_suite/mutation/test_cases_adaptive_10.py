from cut import *

def test_case_0():
	cut = calorie_intake_calc(54.93,172.59,82,'F',-0.45,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 38
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(166.82,199.15,42,'F',-0.27,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.age = 49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 157.57
	cut.age = 18
	cut.height = 143.23
	cut.bodyfat = 0.4
	cut.weight = 38.8

