from cut import *

def test_case_0():
	cut = calorie_intake_calc(153.24,212.98,45,'M',0.15,'E')
	cut.weight = 52.23
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(196.04,143.63,72,'N',0.18,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 146.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(74.23,145.96,21,'M',0.1,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(185.75,156.06,29,'M',0.02,'S')
	cut.weight = 164.19
	cut.weight = 49.07
	cut.age = 75

def test_case_4():
	cut = calorie_intake_calc(207.39,178.48,21,'F',0.12,'E')
	cut.bodyfat = 0.04
	cut.age = 36
	cut.height = 146.01
	cut.bodyfat = 0.08
	cut.bodyfat = 0.13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.height = 172.31
	cut.gender = 'N'

def test_case_5():
	cut = calorie_intake_calc(117.67,174.52,43,'F',0.18,'N')

def test_case_6():
	cut = calorie_intake_calc(134.86,218.64,29,'F',0.15,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.94
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.29
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.height = 197.7

def test_case_7():
	cut = calorie_intake_calc(92.71,167.81,46,'M',0.26,'M')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 37
	cut.height = 211.43
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 205.41
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'

def test_case_8():
	cut = calorie_intake_calc(63.58,176.52,55,'M',0.12,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 32
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 49
	cut.weight = 80.87
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

