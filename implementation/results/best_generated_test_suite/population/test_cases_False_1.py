from cut import *

def test_case_0():
	cut = calorie_intake_calc(74.47,165.29,29,'F',0.16,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	cut.height = 196.77
	cut.weight = 75.82
	cut.weight = 81.84

def test_case_1():
	cut = calorie_intake_calc(207.82,186.01,77,'F',0.28,'M')
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 153.5
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(57.7,196.55,29,'N',0.03,'M')

def test_case_3():
	cut = calorie_intake_calc(183.12,176.01,66,'F',0.19,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

