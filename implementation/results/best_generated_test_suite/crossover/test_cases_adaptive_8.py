from cut import *

def test_case_0():
	cut = calorie_intake_calc(85.28,167.07,58,'M',0.01,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'L'
	cut.weight = 45.26
	cut.age = 45
	cut.age = 20
	cut.bodyfat = 0.12
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(145.29,186.06,44,'F',0.2,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.25
	result_tdee_calculation = cut.tdee_calculation()

