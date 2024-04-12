from cut import *

def test_case_0():
	cut = calorie_intake_calc(123.55,177.7,44,'M',0.12,'E')
	cut.amount_exercise = 'V'
	cut.weight = 112.74
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 46
	cut.amount_exercise = 'E'
	cut.age = 44
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(102.59,170.5,50,'M',0.02,'M')
	cut.weight = 43.39
	cut.height = 156.59
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.age = 24
	cut.height = 180.04
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(93.69,151.32,30,'M',0.16,'E')
	cut.weight = 76.99
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 170.73

