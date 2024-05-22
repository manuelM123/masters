from cut import *

def test_case_0():
	cut = calorie_intake_calc(69.88,165.38,39,'N',0.68,'M')
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 203.11
	cut.height = 214.02
	cut.height = 196.74
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(214.21,217.86,36,'N',0.41,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 67
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.28
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(167.13,188.43,53,'F',-0.24,'L')
	cut.bodyfat = 0.22
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.01
	cut.height = 166.92
	cut.gender = 'M'
	cut.gender = 'N'
	cut.height = 174.15
	cut.bodyfat = -0.45

def test_case_3():
	cut = calorie_intake_calc(174.5,206.23,53,'M',-0.46,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.height = 139.37
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 48.19
	cut.weight = 35.4
	cut.weight = 45.03

def test_case_4():
	cut = calorie_intake_calc(123.6,164.78,82,'M',-0.23,'M')
	cut.bodyfat = 0.38
	cut.weight = 111.19
	cut.bodyfat = -0.27
	cut.bodyfat = -0.13
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	cut.weight = 111.75
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(111.15,159.77,18,'N',0.05,'M')
	cut.amount_exercise = 'N'

def test_case_6():
	cut = calorie_intake_calc(53.15,200.44,31,'M',-0.25,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 57.36
	cut.bodyfat = 0.06
	cut.bodyfat = 0.19

def test_case_7():
	cut = calorie_intake_calc(109.69,189.54,60,'M',0.54,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'

def test_case_8():
	cut = calorie_intake_calc(106.05,219.63,9,'M',-0.07,'N')
	cut.height = 175.38
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 151.05

def test_case_9():
	cut = calorie_intake_calc(51.37,192.43,80,'F',0.24,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 31
	cut.age = 49
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

