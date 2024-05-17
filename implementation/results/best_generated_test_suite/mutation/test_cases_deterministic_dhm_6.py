from cut import *

def test_case_0():
	cut = calorie_intake_calc(118.86,146.69,59,'M',0.53,'L')
	cut.height = 202.42
	cut.amount_exercise = 'L'
	cut.height = 152.25

def test_case_1():
	cut = calorie_intake_calc(46.4,165.19,22,'N',0.48,'V')
	cut.bodyfat = -0.48
	cut.weight = 187.98
	cut.gender = 'N'
	cut.weight = 42.04

def test_case_2():
	cut = calorie_intake_calc(47.34,166.65,67,'N',0.6,'L')
	cut.gender = 'M'
	cut.age = 69
	cut.amount_exercise = 'N'
	cut.gender = 'M'
	cut.height = 143.81
	cut.amount_exercise = 'E'

def test_case_3():
	cut = calorie_intake_calc(87.3,149.93,32,'M',0.4,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(54.89,135.16,5,'M',-0.24,'N')
	cut.gender = 'F'
	cut.bodyfat = -0.27
	cut.age = 41
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.65
	cut.weight = 123.68
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 155.39
	cut.age = 59
	cut.weight = 90.46

def test_case_5():
	cut = calorie_intake_calc(81.3,214.71,63,'N',0.34,'M')
	cut.age = 77
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 112.91
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 52.17

def test_case_6():
	cut = calorie_intake_calc(47.85,210.58,58,'F',-0.08,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(43.72,161.14,15,'N',0.0,'M')
	cut.weight = 38.28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.height = 187.08

def test_case_8():
	cut = calorie_intake_calc(152.16,157.18,17,'F',-0.47,'V')
	cut.gender = 'N'
	cut.bodyfat = -0.37

def test_case_9():
	cut = calorie_intake_calc(86.85,204.26,76,'F',0.67,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.27
	cut.height = 158.6

def test_case_10():
	cut = calorie_intake_calc(214.33,172.23,26,'M',0.32,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.09
	cut.gender = 'N'
	cut.weight = 155.69
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 185.81
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_11():
	cut = calorie_intake_calc(76.54,211.9,66,'M',-0.23,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 32
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

