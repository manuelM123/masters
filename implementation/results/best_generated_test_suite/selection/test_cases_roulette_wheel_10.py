from cut import *

def test_case_0():
	cut = calorie_intake_calc(109.9,216.28,66,'M',-0.21,'V')

def test_case_1():
	cut = calorie_intake_calc(149.14,141.17,36,'M',0.66,'N')
	cut.height = 209.65
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.6
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(80.78,174.86,69,'M',0.04,'E')
	cut.weight = 129.03
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.5
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 185.12
	cut.age = 58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(54.89,197.25,10,'M',0.59,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.bodyfat = 0.43

def test_case_4():
	cut = calorie_intake_calc(56.42,164.32,21,'N',-0.4,'E')
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(200.14,179.39,61,'N',-0.18,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 47

def test_case_6():
	cut = calorie_intake_calc(142.58,179.57,62,'M',-0.19,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 191.17
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 171.48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(159.21,172.18,84,'F',0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.31
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 73
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'

def test_case_8():
	cut = calorie_intake_calc(71.42,175.94,19,'M',0.77,'N')
	cut.age = 37
	cut.weight = 203.06
	cut.weight = 50.29
	cut.height = 164.13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.21
	cut.gender = 'F'
	cut.age = 27

def test_case_9():
	cut = calorie_intake_calc(191.51,164.08,53,'N',-0.02,'N')
	cut.weight = 104.48
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.height = 182.01
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46
	cut.age = 58
	result_determine_calorie_intake = cut.determine_calorie_intake()

