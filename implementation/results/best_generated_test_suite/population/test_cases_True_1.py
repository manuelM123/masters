from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.17,192.17,73,'N',0.08,'E')
	cut.bodyfat = 0.44
	cut.weight = 195.66
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(59.44,135.04,75,'F',-0.25,'V')

def test_case_2():
	cut = calorie_intake_calc(58.99,219.03,62,'M',0.1,'L')
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.42
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(122.65,215.2,30,'F',-0.41,'V')
	cut.bodyfat = 0.2
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.height = 163.5
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 137.26
	cut.weight = 115.75
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.37
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 151.63
	cut.height = 196.23

def test_case_4():
	cut = calorie_intake_calc(60.94,178.59,48,'M',0.01,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 144.58

def test_case_5():
	cut = calorie_intake_calc(66.13,172.0,54,'M',-0.03,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.41
	cut.gender = 'F'
	cut.bodyfat = 0.32
	cut.age = 23
	cut.bodyfat = 0.15
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 7
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 155.33
	cut.gender = 'F'

def test_case_6():
	cut = calorie_intake_calc(177.85,152.17,24,'F',0.8,'V')

def test_case_7():
	cut = calorie_intake_calc(191.77,194.6,11,'M',0.07,'N')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 113.73
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.49
	cut.bodyfat = 0.57

def test_case_8():
	cut = calorie_intake_calc(187.14,199.17,62,'F',-0.34,'M')
	cut.age = 25
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()

