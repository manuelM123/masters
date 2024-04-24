from cut import *

def test_case_0():
	cut = calorie_intake_calc(95.92,206.46,79,'M',0.21,'S')

def test_case_1():
	cut = calorie_intake_calc(67.17,203.64,11,'N',0.12,'E')
	cut.height = 181.33
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 164.94
	cut.amount_exercise = 'N'

def test_case_2():
	cut = calorie_intake_calc(153.37,176.71,37,'F',0.07,'L')
	cut.age = 36
	cut.height = 162.24
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.14

def test_case_3():
	cut = calorie_intake_calc(181.08,150.78,19,'M',0.08,'L')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 173.54
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 45

def test_case_4():
	cut = calorie_intake_calc(99.63,215.98,49,'F',0.07,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(183.12,185.63,47,'F',0.17,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.25
	cut.age = 64
	cut.weight = 191.27
	cut.age = 58

