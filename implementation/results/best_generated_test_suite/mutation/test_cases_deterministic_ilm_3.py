from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.77,192.23,10,'F',0.21,'S')
	cut.height = 146.4
	cut.gender = 'M'
	cut.height = 211.07
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(154.09,156.36,14,'F',0.29,'M')
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(66.0,179.67,12,'M',0.26,'M')
	cut.weight = 115.89
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 60
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(64.6,141.07,59,'M',0.22,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 73.67
	cut.height = 169.7
	cut.bodyfat = 0.23
	cut.age = 52
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.weight = 175.32
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(172.41,184.3,12,'N',0.13,'E')
	cut.bodyfat = 0.07
	cut.bodyfat = 0.27
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(53.35,180.18,13,'F',0.22,'E')
	cut.bodyfat = 0.05
	cut.bodyfat = 0.26
	cut.height = 199.81

def test_case_6():
	cut = calorie_intake_calc(124.69,216.69,76,'M',0.15,'E')

def test_case_7():
	cut = calorie_intake_calc(137.18,169.59,47,'F',0.2,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 181.11
	cut.bodyfat = 0.08
	cut.weight = 87.48
	cut.weight = 206.8
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(166.35,156.43,64,'F',0.25,'M')
	cut.height = 196.08
	cut.age = 21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 75
	cut.amount_exercise = 'V'
	cut.height = 185.15

def test_case_9():
	cut = calorie_intake_calc(90.68,212.33,44,'N',0.28,'V')
	cut.age = 50
	cut.weight = 163.96

