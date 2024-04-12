from cut import *

def test_case_0():
	cut = calorie_intake_calc(91.83,166.5,50,'M',0.23,'V')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(89.97,217.54,81,'F',0.21,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(169.37,162.58,53,'M',0.21,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.05
	cut.height = 195.47
	cut.height = 205.03

def test_case_3():
	cut = calorie_intake_calc(172.27,205.12,55,'M',0.14,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 159.23
	cut.weight = 204.71
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

