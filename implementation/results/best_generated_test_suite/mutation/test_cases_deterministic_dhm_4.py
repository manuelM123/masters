from cut import *

def test_case_0():
	cut = calorie_intake_calc(105.64,184.85,13,'M',0.17,'L')
	cut.bodyfat = 0.15
	cut.weight = 165.11
	cut.gender = 'M'
	cut.age = 58
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.12

def test_case_1():
	cut = calorie_intake_calc(45.6,147.73,29,'N',0.06,'N')
	cut.weight = 43.75
	cut.height = 162.57
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.0
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 190.71
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(117.21,198.55,33,'N',0.3,'V')
	cut.bodyfat = 0.05
	cut.gender = 'M'
	cut.height = 152.66
	cut.height = 216.54
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(99.78,178.65,54,'N',0.25,'L')

def test_case_4():
	cut = calorie_intake_calc(167.47,204.43,60,'F',0.24,'V')

def test_case_5():
	cut = calorie_intake_calc(192.01,185.78,65,'N',0.08,'V')
	cut.height = 194.84
	cut.height = 181.33
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 214.87

def test_case_6():
	cut = calorie_intake_calc(204.06,172.82,65,'M',0.18,'V')
	cut.bodyfat = 0.18
	cut.age = 80
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 119.09
	cut.amount_exercise = 'L'

def test_case_7():
	cut = calorie_intake_calc(203.61,215.86,17,'F',0.09,'E')
	cut.bodyfat = 0.11
	cut.age = 14
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.age = 75

