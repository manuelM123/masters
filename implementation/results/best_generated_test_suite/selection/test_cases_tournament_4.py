from cut import *

def test_case_0():
	cut = calorie_intake_calc(148.34,186.79,35,'M',0.1,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.25
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(204.2,203.99,10,'F',0.27,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

