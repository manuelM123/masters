from cut import *

def test_case_0():
	cut = calorie_intake_calc(101.83,152.25,16,'F',-0.16,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 88.84
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(164.58,137.68,68,'F',0.35,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 150.89
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(153.34,200.18,69,'F',-0.45,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 159.87
	cut.bodyfat = -0.25
	cut.height = 177.5
	cut.bodyfat = 0.62
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(198.39,193.26,11,'F',0.21,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()

