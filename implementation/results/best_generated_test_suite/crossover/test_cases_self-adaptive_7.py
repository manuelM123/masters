from cut import *

def test_case_0():
	cut = calorie_intake_calc(56.04,176.8,76,'F',0.02,'M')
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.14
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(126.03,178.8,33,'F',0.26,'S')
	cut.gender = 'M'
	cut.age = 12
	cut.age = 65
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 180.36
	cut.bodyfat = 0.27
	cut.height = 209.84
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(87.09,174.75,60,'F',0.26,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 191.57
	cut.height = 140.74
	cut.weight = 167.83
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.amount_exercise = 'N'

def test_case_3():
	cut = calorie_intake_calc(125.4,220.1,12,'N',0.27,'S')
	cut.amount_exercise = 'V'
	cut.gender = 'N'
	cut.age = 41
	cut.height = 220.65

def test_case_4():
	cut = calorie_intake_calc(75.78,185.16,50,'M',0.21,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 169.26
	cut.bodyfat = 0.27
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 70
	result_tdee_calculation = cut.tdee_calculation()

