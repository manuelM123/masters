from cut import *

def test_case_0():
	cut = calorie_intake_calc(145.22,210.18,35,'F',0.62,'N')
	cut.weight = 95.95
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 11
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 154.84

def test_case_1():
	cut = calorie_intake_calc(209.89,186.0,80,'N',0.34,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.14
	cut.bodyfat = 0.27
	cut.age = 68
	cut.age = 61
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(125.82,168.21,11,'N',-0.1,'V')

def test_case_3():
	cut = calorie_intake_calc(54.89,197.25,10,'M',0.59,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.bodyfat = 0.43

def test_case_4():
	cut = calorie_intake_calc(74.74,185.44,35,'M',0.43,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 51
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(134.59,202.63,28,'F',-0.45,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.weight = 141.83
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 85

def test_case_6():
	cut = calorie_intake_calc(195.76,211.64,33,'M',-0.13,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	cut.age = 45
	cut.age = 76

def test_case_7():
	cut = calorie_intake_calc(82.16,208.4,58,'N',0.12,'E')
	cut.amount_exercise = 'N'

def test_case_8():
	cut = calorie_intake_calc(100.55,145.0,5,'N',0.7,'E')

def test_case_9():
	cut = calorie_intake_calc(191.51,164.08,53,'N',-0.02,'N')
	cut.weight = 104.48
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.height = 182.01
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 58
	result_determine_calorie_intake = cut.determine_calorie_intake()

