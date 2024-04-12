from cut import *

def test_case_0():
	cut = calorie_intake_calc(96.98,209.39,32,'M',0.01,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(92.98,152.4,42,'M',0.27,'M')
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.age = 47
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(151.36,154.11,10,'N',0.29,'V')
	cut.weight = 136.04
	cut.height = 149.47
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 48
	cut.gender = 'F'
	cut.height = 156.57

def test_case_3():
	cut = calorie_intake_calc(42.5,172.35,81,'F',0.22,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 46
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 161.09
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_4():
	cut = calorie_intake_calc(145.83,154.94,44,'N',0.07,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 193.59
	cut.bodyfat = 0.28
	cut.bodyfat = 0.04
	cut.age = 81
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 76.06

