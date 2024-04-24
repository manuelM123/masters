from cut import *

def test_case_0():
	cut = calorie_intake_calc(184.83,209.49,55,'M',0.16,'S')
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(173.19,164.7,63,'F',0.19,'V')
	cut.amount_exercise = 'E'

def test_case_2():
	cut = calorie_intake_calc(161.65,207.41,59,'F',0.28,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 197.63
	cut.gender = 'N'
	cut.weight = 66.65

def test_case_3():
	cut = calorie_intake_calc(49.32,199.1,18,'F',0.04,'M')
	cut.bodyfat = 0.02
	cut.height = 157.43
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'

def test_case_4():
	cut = calorie_intake_calc(107.15,200.72,37,'M',0.25,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 67
	cut.age = 78
	cut.age = 35
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 148.95
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

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

