from cut import *

def test_case_0():
	cut = calorie_intake_calc(124.96,166.24,24,'F',0.1,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.age = 52
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(53.6,186.27,41,'F',0.16,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 204.49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(167.31,203.46,35,'M',0.12,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.04
	result_tdee_calculation = cut.tdee_calculation()

