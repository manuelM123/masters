from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.44,135.9,41,'N',0.34,'S')
	cut.bodyfat = -0.31
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(189.2,160.34,44,'M',-0.28,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.78
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 19

def test_case_2():
	cut = calorie_intake_calc(102.67,188.16,76,'F',0.29,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.height = 220.97

