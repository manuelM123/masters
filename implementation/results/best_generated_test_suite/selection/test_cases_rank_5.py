from cut import *

def test_case_0():
	cut = calorie_intake_calc(156.12,192.66,57,'F',0.04,'V')
	cut.bodyfat = 0.27
	cut.gender = 'N'
	cut.age = 50
	cut.weight = 169.0
	cut.gender = 'M'
	cut.bodyfat = 0.01

def test_case_1():
	cut = calorie_intake_calc(179.56,184.94,46,'F',0.13,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 75
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(186.48,216.72,11,'F',0.04,'E')
	cut.height = 217.2
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.02
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(210.8,172.83,40,'N',0.23,'M')
	cut.gender = 'N'
	cut.gender = 'M'
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(152.91,142.42,73,'M',0.18,'S')
	cut.height = 170.6
	cut.height = 211.4
	cut.bodyfat = 0.16
	cut.bodyfat = 0.02
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.13
	cut.bodyfat = 0.29

def test_case_5():
	cut = calorie_intake_calc(155.7,203.83,46,'F',0.24,'N')
	cut.age = 80

def test_case_6():
	cut = calorie_intake_calc(45.42,189.2,37,'M',0.06,'E')
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 56
	cut.amount_exercise = 'V'
	cut.weight = 203.83
	cut.bodyfat = 0.07
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.weight = 157.64

def test_case_7():
	cut = calorie_intake_calc(200.49,156.95,13,'M',0.16,'N')
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 93.39
	cut.bodyfat = 0.12
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_8():
	cut = calorie_intake_calc(132.17,182.12,61,'N',0.1,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.age = 68
	cut.bodyfat = 0.23

def test_case_9():
	cut = calorie_intake_calc(40.49,184.02,63,'F',0.23,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 97.1
	cut.height = 196.84
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_10():
	cut = calorie_intake_calc(73.32,196.05,10,'N',0.08,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 97.83
	cut.height = 151.67
	cut.age = 69

def test_case_11():
	cut = calorie_intake_calc(119.81,147.48,58,'M',0.25,'M')
	cut.age = 12
	cut.height = 193.49
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 21
	cut.age = 43

def test_case_12():
	cut = calorie_intake_calc(199.12,187.64,52,'F',0.21,'S')

def test_case_13():
	cut = calorie_intake_calc(76.04,170.89,66,'N',0.22,'N')
	cut.age = 80
	cut.bodyfat = 0.14
	cut.bodyfat = 0.08
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 63
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

