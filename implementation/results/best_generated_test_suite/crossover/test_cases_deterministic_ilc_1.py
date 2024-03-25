from cut import *

def test_case_0():
	cut = calorie_intake_calc(121.68,213.83,21,'M',0.18,'M')
	cut.bodyfat = 0.12
	cut.height = 209.54
	cut.bodyfat = 0.17
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 144.79
	cut.weight = 57.75
	cut.gender = 'M'
	cut.height = 214.04
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(182.83,206.91,73,'M',0.14,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.3
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 201.74
	cut.age = 53
	cut.amount_exercise = 'S'

def test_case_2():
	cut = calorie_intake_calc(140.2,181.03,49,'F',0.27,'S')
	cut.bodyfat = 0.19
	cut.weight = 137.18
	cut.gender = 'N'
	cut.age = 19
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(172.38,180.99,62,'M',0.22,'V')
	cut.weight = 168.82

def test_case_4():
	cut = calorie_intake_calc(169.95,153.9,47,'F',0.22,'V')
	cut.height = 209.92
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 22

