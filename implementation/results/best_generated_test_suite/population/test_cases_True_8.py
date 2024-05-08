from cut import *

def test_case_0():
	cut = calorie_intake_calc(69.4,157.76,19,'F',0.18,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 66
	cut.age = 64
	cut.age = 82
	cut.bodyfat = 0.46
	cut.amount_exercise = 'L'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 143.65

def test_case_1():
	cut = calorie_intake_calc(143.43,201.77,77,'M',0.42,'M')
	cut.bodyfat = 0.68
	cut.height = 163.75
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 182.79
	cut.age = 16
	cut.amount_exercise = 'M'

def test_case_2():
	cut = calorie_intake_calc(48.1,158.02,18,'M',-0.19,'L')
	cut.bodyfat = -0.21
	cut.weight = 152.1
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(116.5,209.62,19,'N',0.57,'S')
	cut.amount_exercise = 'N'
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.53

def test_case_4():
	cut = calorie_intake_calc(164.05,212.38,23,'N',0.16,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

def test_case_5():
	cut = calorie_intake_calc(131.22,180.4,52,'M',0.18,'M')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	cut.height = 158.76
	cut.amount_exercise = 'L'
	cut.age = 53
	cut.weight = 202.3
	cut.height = 175.52
	cut.weight = 93.45

def test_case_6():
	cut = calorie_intake_calc(186.34,192.96,36,'F',-0.33,'E')
	cut.weight = 79.91
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 163.85
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.37
	cut.bodyfat = 0.24

def test_case_7():
	cut = calorie_intake_calc(184.58,136.74,60,'F',0.58,'S')

def test_case_8():
	cut = calorie_intake_calc(153.64,195.88,39,'N',0.52,'V')
	cut.amount_exercise = 'M'
	cut.bodyfat = -0.16

