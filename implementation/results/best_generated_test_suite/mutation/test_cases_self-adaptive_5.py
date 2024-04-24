from cut import *

def test_case_0():
	cut = calorie_intake_calc(145.31,154.58,17,'F',0.19,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(127.18,186.16,74,'M',0.25,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(125.39,140.02,37,'F',0.17,'N')
	cut.weight = 153.1
	cut.age = 58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 30
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'

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
	cut = calorie_intake_calc(100.31,151.75,62,'M',0.03,'E')
	cut.gender = 'M'
	cut.gender = 'M'

def test_case_5():
	cut = calorie_intake_calc(154.17,194.03,80,'M',0.15,'N')
	cut.height = 177.17

def test_case_6():
	cut = calorie_intake_calc(128.55,148.01,47,'M',0.24,'L')
	cut.height = 198.29
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 97.3
	cut.age = 55
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 35

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

