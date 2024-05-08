from cut import *

def test_case_0():
	cut = calorie_intake_calc(47.85,152.75,60,'M',-0.46,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 206.8
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 68.83
	cut.weight = 48.22

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
	cut = calorie_intake_calc(77.96,173.04,60,'F',0.01,'N')

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
	cut = calorie_intake_calc(192.49,220.67,66,'N',0.36,'V')
	cut.height = 215.65
	result_tdee_calculation = cut.tdee_calculation()

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
	cut = calorie_intake_calc(175.5,144.22,57,'F',0.3,'M')
	cut.height = 174.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 85
	cut.age = 60
	cut.age = 23

