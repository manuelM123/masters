from cut import *

def test_case_0():
	cut = calorie_intake_calc(82.34,136.18,66,'N',-0.01,'N')
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.46
	cut.bodyfat = 0.59

def test_case_1():
	cut = calorie_intake_calc(148.4,222.85,45,'M',-0.03,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.41

