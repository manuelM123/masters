from cut import *

def test_case_0():
	cut = calorie_intake_calc(82.12,143.81,24,'N',0.1,'L')
	cut.bodyfat = 0.13
	cut.bodyfat = 0.06
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.17
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 84.04
	cut.bodyfat = 0.19
	cut.amount_exercise = 'E'

def test_case_1():
	cut = calorie_intake_calc(53.15,170.9,51,'F',0.05,'E')
	cut.weight = 166.46
	cut.age = 13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.age = 10
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(162.0,179.54,47,'M',0.28,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 155.87
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 201.67
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.27
	cut.bodyfat = 0.01
	cut.amount_exercise = 'N'
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(88.66,161.36,60,'F',0.06,'L')
	cut.height = 195.1
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.11
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.13
	cut.weight = 163.29
	cut.gender = 'F'
	cut.age = 64

def test_case_4():
	cut = calorie_intake_calc(72.63,170.98,32,'F',0.2,'S')
	cut.weight = 48.14
	cut.bodyfat = 0.21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(79.52,154.65,75,'N',0.07,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 40
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10

def test_case_6():
	cut = calorie_intake_calc(118.84,220.23,17,'F',0.15,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.01
	cut.age = 25
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

