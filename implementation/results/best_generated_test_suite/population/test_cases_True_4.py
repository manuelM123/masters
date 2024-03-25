from cut import *

def test_case_0():
	cut = calorie_intake_calc(118.59,180.4,47,'M',0.29,'E')
	cut.age = 76
	cut.bodyfat = 0.21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 164.59
	cut.bodyfat = 0.1
	cut.gender = 'F'
	cut.weight = 93.12

def test_case_1():
	cut = calorie_intake_calc(115.15,142.1,46,'M',0.2,'V')
	cut.weight = 176.96
	cut.height = 174.64
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'M'
	cut.age = 44

def test_case_2():
	cut = calorie_intake_calc(112.01,214.86,62,'N',0.21,'V')
	cut.weight = 78.96

def test_case_3():
	cut = calorie_intake_calc(124.68,151.73,63,'F',0.08,'N')
	cut.gender = 'M'
	cut.height = 170.15

def test_case_4():
	cut = calorie_intake_calc(83.53,186.48,63,'M',0.2,'S')
	cut.weight = 54.34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 190.42
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.14

