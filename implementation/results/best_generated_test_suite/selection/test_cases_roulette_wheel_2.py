from cut import *

def test_case_0():
	cut = calorie_intake_calc(141.89,170.23,54,'N',0.06,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 158.73
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(109.69,152.78,58,'N',0.23,'S')
	cut.weight = 67.18
	cut.amount_exercise = 'M'

def test_case_2():
	cut = calorie_intake_calc(73.04,175.69,77,'M',0.22,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.07
	cut.age = 76
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 62
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(179.06,162.55,32,'F',0.25,'M')
	cut.weight = 90.88
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 147.0
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'

def test_case_4():
	cut = calorie_intake_calc(144.78,205.52,37,'F',0.24,'N')
	cut.weight = 66.62
	cut.bodyfat = 0.04

