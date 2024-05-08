from cut import *

def test_case_0():
	cut = calorie_intake_calc(124.69,220.25,28,'N',-0.31,'M')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(40.51,223.74,14,'M',0.78,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.3
	cut.height = 209.23
	cut.age = 39
	cut.gender = 'M'
	cut.gender = 'N'
	cut.height = 144.18
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 129.93

def test_case_2():
	cut = calorie_intake_calc(63.65,213.14,5,'M',0.65,'L')
	cut.amount_exercise = 'N'
	cut.weight = 205.52
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'

def test_case_3():
	cut = calorie_intake_calc(110.04,218.71,43,'M',0.02,'E')
	cut.bodyfat = -0.46
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 80
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

