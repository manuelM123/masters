from cut import *

def test_case_0():
	cut = calorie_intake_calc(210.89,199.49,41,'N',0.26,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 208.58
	cut.gender = 'N'

def test_case_1():
	cut = calorie_intake_calc(182.61,203.51,57,'F',0.14,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(201.93,185.73,26,'F',0.08,'M')
	cut.gender = 'M'
	cut.height = 161.51
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.height = 162.94

def test_case_3():
	cut = calorie_intake_calc(70.12,220.23,76,'F',0.05,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 79
	cut.bodyfat = 0.03

def test_case_4():
	cut = calorie_intake_calc(128.08,198.81,64,'M',0.05,'L')
	cut.age = 41
	cut.gender = 'M'
	cut.gender = 'M'
	cut.height = 198.37
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(191.08,148.64,42,'F',0.18,'E')
	cut.amount_exercise = 'N'

def test_case_6():
	cut = calorie_intake_calc(195.85,168.59,50,'M',0.16,'E')
	cut.age = 34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 181.48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 161.82
	cut.gender = 'F'
	cut.bodyfat = 0.21
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 198.38

def test_case_7():
	cut = calorie_intake_calc(208.59,159.47,36,'F',0.21,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.28
	cut.weight = 177.17
	cut.bodyfat = 0.29
	cut.weight = 122.68
	cut.weight = 143.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

