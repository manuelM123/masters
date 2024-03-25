from cut import *

def test_case_0():
	cut = calorie_intake_calc(177.08,149.8,45,'M',0.24,'N')
	cut.gender = 'N'
	cut.gender = 'M'
	cut.height = 167.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 140.74
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 54.38
	cut.bodyfat = 0.05
	cut.height = 160.28

def test_case_1():
	cut = calorie_intake_calc(113.86,167.26,70,'F',0.17,'E')
	cut.bodyfat = 0.19
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(99.41,188.08,11,'M',0.01,'V')
	cut.age = 35
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.08
	cut.age = 12
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.26
	cut.height = 172.38
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.18

