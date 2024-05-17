from cut import *

def test_case_0():
	cut = calorie_intake_calc(124.38,198.93,12,'F',-0.1,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75

def test_case_1():
	cut = calorie_intake_calc(179.25,206.2,25,'M',0.06,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 45
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.04
	cut.bodyfat = 0.23
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(76.82,181.72,32,'F',0.13,'M')
	cut.height = 149.47
	cut.height = 143.51
	cut.age = 5
	result_determine_calorie_intake = cut.determine_calorie_intake()

