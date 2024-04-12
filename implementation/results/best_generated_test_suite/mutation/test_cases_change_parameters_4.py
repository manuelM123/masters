from cut import *

def test_case_0():
	cut = calorie_intake_calc(103.03,204.7,20,'F',0.27,'E')
	cut.bodyfat = 0.12
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.age = 70
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(179.73,207.93,35,'F',0.01,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 90.44
	cut.weight = 70.17
	cut.bodyfat = 0.07
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.28

