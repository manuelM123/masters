from cut import *

def test_case_0():
	cut = calorie_intake_calc(122.81,177.67,71,'M',0.09,'S')
	cut.bodyfat = 0.27
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'

def test_case_1():
	cut = calorie_intake_calc(206.9,201.97,37,'N',0.22,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.height = 216.95
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(118.32,152.98,36,'M',0.12,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.17
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(60.54,168.8,28,'N',0.15,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 169.64
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 183.23
	cut.bodyfat = 0.1
	cut.height = 190.47
	cut.amount_exercise = 'N'

