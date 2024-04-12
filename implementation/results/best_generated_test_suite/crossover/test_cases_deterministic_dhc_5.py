from cut import *

def test_case_0():
	cut = calorie_intake_calc(128.8,179.06,16,'M',0.16,'E')
	cut.height = 191.51
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	cut.age = 68
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(65.37,211.22,39,'F',0.16,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.2

