from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.14,217.46,15,'F',0.21,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(156.77,187.42,64,'F',0.16,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 76
	cut.age = 65
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 163.47

def test_case_2():
	cut = calorie_intake_calc(158.3,219.14,52,'M',0.12,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(55.53,194.08,13,'M',0.28,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 57.09
	cut.height = 181.17
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(64.08,160.37,46,'F',0.18,'M')

def test_case_5():
	cut = calorie_intake_calc(161.46,146.81,59,'M',0.12,'E')
	cut.height = 192.92
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 85.07
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.2
	cut.amount_exercise = 'N'
	cut.age = 30
	cut.age = 46
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(114.72,215.88,21,'F',0.13,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.height = 146.17
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 164.42
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'N'

