from cut import *

def test_case_0():
	cut = calorie_intake_calc(97.27,184.79,45,'M',0.2,'M')
	cut.weight = 173.52
	cut.bodyfat = 0.24
	cut.weight = 139.25
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 157.37
	cut.weight = 189.0
	cut.age = 16
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(122.21,205.6,69,'M',0.12,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 44

def test_case_2():
	cut = calorie_intake_calc(55.05,154.88,49,'M',0.24,'E')
	cut.bodyfat = 0.01
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(82.29,189.71,20,'N',0.27,'V')
	cut.weight = 163.02
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.19
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.21
	cut.weight = 101.99

def test_case_4():
	cut = calorie_intake_calc(75.47,194.36,49,'M',0.17,'N')
	cut.amount_exercise = 'V'
	cut.weight = 93.67
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 79.06

def test_case_5():
	cut = calorie_intake_calc(196.84,158.42,19,'N',0.11,'S')
	cut.age = 46
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 35
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

def test_case_6():
	cut = calorie_intake_calc(195.85,168.59,50,'M',0.16,'E')
	cut.age = 34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 181.48
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 161.82
	cut.gender = 'F'
	cut.bodyfat = 0.21
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 198.38

def test_case_7():
	cut = calorie_intake_calc(60.6,209.52,43,'F',0.26,'V')
	cut.weight = 150.3
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.3

