from cut import *

def test_case_0():
	cut = calorie_intake_calc(96.89,196.16,27,'M',0.1,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(169.85,152.62,29,'M',0.03,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(56.29,184.69,19,'M',0.1,'N')
	cut.age = 24
	cut.amount_exercise = 'N'

