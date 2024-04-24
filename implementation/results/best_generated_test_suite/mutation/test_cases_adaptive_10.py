from cut import *

def test_case_0():
	cut = calorie_intake_calc(115.6,170.95,13,'F',0.04,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.13
	cut.age = 30
	cut.height = 154.37
	cut.bodyfat = 0.29

def test_case_1():
	cut = calorie_intake_calc(206.22,176.77,30,'N',0.04,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	cut.height = 216.64
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 22

def test_case_2():
	cut = calorie_intake_calc(165.98,199.66,73,'M',0.08,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.17
	cut.gender = 'F'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(177.32,178.11,56,'F',0.18,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(93.11,220.07,68,'F',0.03,'M')
	cut.age = 45
	cut.bodyfat = 0.1

