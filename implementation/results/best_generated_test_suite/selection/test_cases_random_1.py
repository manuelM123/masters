from cut import *

def test_case_0():
	cut = calorie_intake_calc(196.32,145.59,63,'N',0.27,'L')
	cut.height = 156.36
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(114.45,185.84,71,'M',0.03,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 72
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 65
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 172.84

def test_case_2():
	cut = calorie_intake_calc(207.14,170.64,20,'M',0.03,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(188.12,208.96,46,'N',0.07,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 72

def test_case_4():
	cut = calorie_intake_calc(157.66,210.46,17,'F',0.27,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	cut.weight = 131.27
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 22
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

