from cut import *

def test_case_0():
	cut = calorie_intake_calc(120.7,192.8,47,'M',0.18,'N')
	cut.weight = 195.49
	cut.bodyfat = -0.0
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(61.76,200.93,40,'M',0.08,'V')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	cut.bodyfat = 0.75
	cut.weight = 131.76
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(95.8,142.18,43,'M',0.51,'N')

def test_case_3():
	cut = calorie_intake_calc(69.19,136.51,21,'M',-0.28,'N')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(74.46,180.87,81,'F',-0.23,'M')
	cut.weight = 165.34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 60
	cut.bodyfat = 0.08
	cut.age = 5
	cut.weight = 177.76
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

