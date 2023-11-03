from cut import *

def test_case_0():
	cut = calorie_intake_calc(111.45,197.12,31,'N',0.07,'M')
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 162.51
	cut.weight = 77.92

def test_case_1():
	cut = calorie_intake_calc(146.31,150.03,34,'F',0.26,'M')
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(111.93,160.13,55,'N',0.22,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(144.07,169.91,21,'F',0.06,'M')
	cut.height = 164.72
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.15

def test_case_4():
	cut = calorie_intake_calc(41.34,192.65,76,'M',0.27,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 56
	cut.age = 71
	cut.weight = 78.74

def test_case_5():
	cut = calorie_intake_calc(166.31,155.56,11,'M',0.1,'S')
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.09

def test_case_6():
	cut = calorie_intake_calc(72.37,154.2,78,'M',0.03,'E')

def test_case_7():
	cut = calorie_intake_calc(183.91,190.72,36,'F',0.19,'E')
	cut.gender = 'N'
	cut.height = 143.89
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(113.93,165.73,81,'N',0.2,'S')
	cut.bodyfat = 0.08
	cut.amount_exercise = 'N'
	cut.age = 22
	cut.age = 52

def test_case_9():
	cut = calorie_intake_calc(102.29,156.57,78,'F',0.11,'M')
	cut.age = 48
	cut.age = 59

def test_case_10():
	cut = calorie_intake_calc(105.18,140.4,60,'F',0.04,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 214.01

