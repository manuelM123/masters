from cut import *

def test_case_0():
	cut = calorie_intake_calc(184.83,209.49,55,'M',0.16,'S')
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(173.19,164.7,63,'F',0.19,'V')
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(198.94,150.31,41,'N',0.3,'S')
	cut.height = 206.85
	cut.bodyfat = 0.05
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'

def test_case_3():
	cut = calorie_intake_calc(122.27,220.38,50,'M',0.18,'V')
	cut.age = 72
	cut.bodyfat = 0.24
	cut.bodyfat = 0.17
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(103.62,173.19,38,'F',0.24,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 80
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.08

def test_case_5():
	cut = calorie_intake_calc(200.99,191.45,76,'M',0.12,'L')
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.height = 188.79
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(43.25,216.7,33,'N',0.28,'M')
	cut.age = 29
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(62.87,145.79,49,'N',0.04,'V')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.weight = 84.98
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

