from cut import *

def test_case_0():
	cut = calorie_intake_calc(152.77,192.23,10,'F',0.21,'S')
	cut.height = 146.4
	cut.gender = 'M'
	cut.height = 211.07
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(154.09,156.36,14,'F',0.29,'M')
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(105.49,163.83,56,'F',0.08,'S')
	cut.weight = 152.23
	cut.weight = 61.12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 118.43
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	cut.bodyfat = 0.17
	cut.height = 182.24
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 214.54

def test_case_3():
	cut = calorie_intake_calc(64.6,141.07,59,'M',0.22,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 73.67
	cut.height = 169.7
	cut.bodyfat = 0.23
	cut.age = 52
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.weight = 175.32
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(118.65,181.54,63,'M',0.18,'S')
	cut.weight = 206.54
	cut.bodyfat = 0.24
	cut.bodyfat = 0.09
	cut.bodyfat = 0.22
	cut.height = 183.16
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.15

def test_case_5():
	cut = calorie_intake_calc(53.35,180.18,13,'F',0.22,'E')
	cut.bodyfat = 0.05
	cut.bodyfat = 0.26
	cut.height = 199.81

def test_case_6():
	cut = calorie_intake_calc(99.02,158.92,33,'N',0.07,'L')
	cut.weight = 49.31
	cut.bodyfat = 0.14
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 101.23

def test_case_7():
	cut = calorie_intake_calc(137.18,169.59,47,'F',0.2,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 181.11
	cut.bodyfat = 0.08
	cut.weight = 87.48
	cut.weight = 206.8
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(48.72,192.29,31,'F',0.18,'E')
	cut.bodyfat = 0.11
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 115.59
	cut.age = 61
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 158.44
	cut.amount_exercise = 'L'
	cut.weight = 104.91

