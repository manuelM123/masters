from cut import *

def test_case_0():
	cut = calorie_intake_calc(81.53,209.38,68,'M',0.0,'V')
	cut.bodyfat = -0.27
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 39
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.51
	cut.weight = 167.88
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(74.04,158.81,29,'N',0.7,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.19
	cut.weight = 83.2
	cut.height = 146.98
	cut.weight = 56.27

def test_case_2():
	cut = calorie_intake_calc(169.39,182.98,39,'M',-0.2,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 174.87
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 79
	cut.height = 186.96
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

