from cut import *

def test_case_0():
	cut = calorie_intake_calc(182.41,145.52,47,'M',0.15,'L')
	cut.gender = 'F'
	cut.bodyfat = 0.28
	cut.height = 142.4
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 179.2
	cut.weight = 207.7
	cut.weight = 166.94
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(113.58,185.77,18,'F',0.1,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.3
	cut.gender = 'F'
	cut.bodyfat = 0.24

def test_case_2():
	cut = calorie_intake_calc(170.7,148.07,44,'M',0.17,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 159.93
	cut.bodyfat = 0.26
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.bodyfat = 0.06
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'

def test_case_3():
	cut = calorie_intake_calc(88.68,182.95,69,'F',0.08,'S')

def test_case_4():
	cut = calorie_intake_calc(93.93,141.21,65,'N',0.24,'S')
	cut.height = 181.38
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 38
	cut.bodyfat = 0.13
	cut.amount_exercise = 'V'
	cut.weight = 130.88
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.age = 15

def test_case_5():
	cut = calorie_intake_calc(116.72,215.79,47,'F',0.13,'S')
	cut.age = 76
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 59
	cut.weight = 117.04
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19
	cut.amount_exercise = 'S'

def test_case_6():
	cut = calorie_intake_calc(83.49,186.42,28,'M',0.28,'E')
	cut.height = 167.87
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 80.23
	cut.amount_exercise = 'V'
	cut.height = 186.92
	cut.weight = 52.99
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'

