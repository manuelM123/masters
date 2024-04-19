from cut import *

def test_case_0():
	cut = calorie_intake_calc(100.32,156.24,75,'N',0.21,'E')
	cut.amount_exercise = 'V'
	cut.height = 182.59
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(207.49,140.48,18,'F',0.13,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.28

def test_case_2():
	cut = calorie_intake_calc(50.66,209.92,33,'M',0.18,'M')
	cut.weight = 152.32
	cut.weight = 179.79
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 175.45
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(85.79,189.67,15,'N',0.01,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 171.46
	cut.height = 205.44

