from cut import *

def test_case_0():
	cut = calorie_intake_calc(130.66,146.32,18,'N',0.32,'M')
	cut.amount_exercise = 'M'
	cut.age = 66
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(37.98,144.17,32,'F',0.39,'S')
	cut.bodyfat = 0.28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 207.11
	cut.bodyfat = 0.46

def test_case_3():
	cut = calorie_intake_calc(112.12,153.12,40,'M',-0.21,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.06
	cut.gender = 'N'
	cut.height = 168.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(126.46,139.76,11,'N',0.17,'M')
	cut.gender = 'F'
	cut.age = 83

