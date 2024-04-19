from cut import *

def test_case_0():
	cut = calorie_intake_calc(149.83,144.41,65,'F',0.04,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 212.85
	cut.weight = 155.59

def test_case_1():
	cut = calorie_intake_calc(207.99,157.96,50,'M',0.02,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(66.0,179.67,12,'M',0.26,'M')
	cut.weight = 115.89
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 60
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(52.09,161.82,65,'M',0.17,'N')
	cut.gender = 'N'
	cut.weight = 150.34
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.13
	cut.bodyfat = 0.03
	cut.gender = 'M'
	cut.age = 14
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(172.41,184.3,12,'N',0.13,'E')
	cut.bodyfat = 0.07
	cut.bodyfat = 0.27
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(98.7,192.92,16,'F',0.22,'L')

def test_case_6():
	cut = calorie_intake_calc(124.69,216.69,76,'M',0.15,'E')

def test_case_7():
	cut = calorie_intake_calc(149.6,209.94,46,'M',0.13,'N')
	cut.age = 48
	cut.weight = 51.43
	cut.height = 187.73
	cut.weight = 184.78
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	cut.weight = 90.68
	cut.gender = 'F'
	cut.bodyfat = 0.03

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

