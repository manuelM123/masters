from cut import *

def test_case_0():
	cut = calorie_intake_calc(88.81,215.7,82,'N',-0.23,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 143.77
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 143.4
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.bodyfat = 0.16
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(72.61,172.21,68,'F',0.29,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(74.48,154.56,44,'F',0.72,'L')
	cut.bodyfat = -0.16
	cut.bodyfat = 0.57
	cut.weight = 72.07
	cut.height = 223.52
	cut.bodyfat = 0.41

def test_case_3():
	cut = calorie_intake_calc(157.95,205.75,19,'F',0.59,'M')
	cut.bodyfat = 0.65
	cut.weight = 104.51
	cut.age = 14
	cut.gender = 'F'
	cut.height = 163.72
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_4():
	cut = calorie_intake_calc(155.19,208.04,27,'F',-0.35,'V')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 150.19

def test_case_5():
	cut = calorie_intake_calc(108.3,211.12,74,'M',0.74,'L')
	cut.weight = 73.46
	cut.gender = 'N'
	cut.height = 164.74
	cut.gender = 'F'
	cut.weight = 116.3

