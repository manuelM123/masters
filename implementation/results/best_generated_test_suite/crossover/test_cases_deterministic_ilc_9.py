from cut import *

def test_case_0():
	cut = calorie_intake_calc(196.21,139.97,49,'F',0.79,'N')
	cut.age = 43
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 15
	cut.weight = 133.72

def test_case_1():
	cut = calorie_intake_calc(67.79,178.59,28,'N',0.44,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 142.1

def test_case_2():
	cut = calorie_intake_calc(192.86,152.76,25,'F',-0.31,'E')
	cut.amount_exercise = 'E'
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.7
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(53.56,211.93,42,'F',0.15,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'E'
	cut.bodyfat = -0.33
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_4():
	cut = calorie_intake_calc(76.04,172.63,42,'F',0.03,'V')
	cut.gender = 'N'
	cut.height = 200.06
	cut.gender = 'N'
	cut.age = 23
	cut.weight = 210.2

def test_case_5():
	cut = calorie_intake_calc(214.36,154.87,35,'M',-0.16,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 221.25
	cut.bodyfat = 0.0
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'

def test_case_6():
	cut = calorie_intake_calc(46.25,185.07,54,'F',0.39,'N')
	cut.weight = 209.25
	cut.height = 136.39
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46
	cut.bodyfat = -0.29

def test_case_7():
	cut = calorie_intake_calc(81.7,215.28,10,'M',0.45,'E')
	cut.amount_exercise = 'S'
	cut.height = 221.55
	cut.age = 68
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 61.29

def test_case_8():
	cut = calorie_intake_calc(150.0,224.03,69,'N',0.09,'V')
	cut.amount_exercise = 'M'
	cut.height = 170.65
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_9():
	cut = calorie_intake_calc(36.29,157.49,69,'M',0.63,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 48.01
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.52

