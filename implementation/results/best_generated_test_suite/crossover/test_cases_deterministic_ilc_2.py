from cut import *

def test_case_0():
	cut = calorie_intake_calc(154.3,189.19,51,'N',0.28,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 61
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 208.84
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 60
	cut.bodyfat = 0.15

def test_case_1():
	cut = calorie_intake_calc(142.9,193.13,33,'M',0.24,'L')
	cut.gender = 'F'
	cut.weight = 141.44
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(121.26,189.27,55,'F',0.03,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.21
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 105.75
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(131.27,191.24,73,'M',0.08,'E')
	cut.height = 199.22
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 49
	cut.age = 79
	result_determine_calorie_intake = cut.determine_calorie_intake()

