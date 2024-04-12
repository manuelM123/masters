from cut import *

def test_case_0():
	cut = calorie_intake_calc(54.03,142.36,31,'F',0.27,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.15
	cut.gender = 'M'
	cut.age = 57

def test_case_1():
	cut = calorie_intake_calc(103.44,198.0,16,'M',0.22,'N')
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 125.94
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.24
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(209.16,161.55,42,'N',0.28,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 38
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.04
	cut.age = 42
	cut.age = 50
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(53.58,153.06,78,'M',0.22,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.25

