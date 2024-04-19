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
	cut = calorie_intake_calc(127.18,186.16,74,'M',0.25,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(125.39,140.02,37,'F',0.17,'N')
	cut.weight = 153.1
	cut.age = 58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 30
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'

def test_case_3():
	cut = calorie_intake_calc(177.32,178.11,56,'F',0.18,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(100.31,151.75,62,'M',0.03,'E')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(168.84,177.17,28,'M',0.12,'M')

def test_case_6():
	cut = calorie_intake_calc(166.18,184.04,49,'N',0.09,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 40
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.21
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 208.48

