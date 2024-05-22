from cut import *

def test_case_0():
	cut = calorie_intake_calc(128.11,185.33,44,'F',0.13,'E')
	cut.weight = 58.69
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 208.9
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 149.34
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'

def test_case_1():
	cut = calorie_intake_calc(172.31,212.42,15,'M',-0.12,'V')
	cut.height = 152.21
	cut.weight = 51.45
	cut.amount_exercise = 'S'

def test_case_2():
	cut = calorie_intake_calc(90.15,195.02,21,'M',-0.2,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.height = 147.48
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 134.78

def test_case_3():
	cut = calorie_intake_calc(108.04,188.22,32,'M',0.66,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.1
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 65.01
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.37
	cut.bodyfat = -0.44
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(112.17,181.08,42,'M',0.24,'E')
	cut.age = 73
	cut.gender = 'M'
	cut.height = 154.52
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 198.59
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.02

def test_case_5():
	cut = calorie_intake_calc(97.31,201.99,47,'M',-0.06,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 210.46
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'

def test_case_6():
	cut = calorie_intake_calc(163.34,136.48,39,'N',0.63,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(39.85,160.79,49,'M',-0.38,'V')
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(213.37,216.96,49,'F',-0.4,'M')
	cut.bodyfat = -0.27
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 71
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 55
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 38
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

