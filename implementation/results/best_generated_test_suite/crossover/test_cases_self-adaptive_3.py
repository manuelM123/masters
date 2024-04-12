from cut import *

def test_case_0():
	cut = calorie_intake_calc(192.33,185.48,70,'N',0.06,'L')
	cut.weight = 156.72
	cut.age = 43

def test_case_1():
	cut = calorie_intake_calc(66.18,173.74,74,'M',0.19,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(154.89,186.81,54,'F',0.13,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 65.57
	cut.age = 20
	cut.weight = 89.01
	cut.age = 32

def test_case_3():
	cut = calorie_intake_calc(113.92,189.14,68,'M',0.24,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_4():
	cut = calorie_intake_calc(176.47,185.67,53,'M',0.19,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 206.25
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(106.73,172.82,68,'F',0.12,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 183.95
	cut.height = 167.2
	cut.age = 80
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.age = 56

