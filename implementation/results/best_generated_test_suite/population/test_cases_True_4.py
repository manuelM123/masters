from cut import *

def test_case_0():
	cut = calorie_intake_calc(117.13,147.71,47,'F',0.13,'M')
	cut.bodyfat = 0.11
	cut.bodyfat = 0.16
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.03

def test_case_1():
	cut = calorie_intake_calc(173.94,214.12,71,'F',0.2,'N')
	cut.height = 205.47

def test_case_2():
	cut = calorie_intake_calc(143.64,204.95,56,'N',0.22,'S')
	cut.gender = 'N'
	cut.height = 160.52
	cut.age = 18
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.19

def test_case_3():
	cut = calorie_intake_calc(197.25,161.63,65,'F',0.2,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 193.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 67
	cut.gender = 'M'
	cut.amount_exercise = 'L'

def test_case_4():
	cut = calorie_intake_calc(67.15,146.77,62,'M',0.04,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 170.9
	cut.amount_exercise = 'S'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.28
	cut.amount_exercise = 'N'
	cut.age = 29
	cut.age = 35

def test_case_5():
	cut = calorie_intake_calc(60.54,182.72,67,'N',0.16,'L')
	cut.height = 181.41
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_6():
	cut = calorie_intake_calc(200.29,203.16,42,'M',0.05,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(123.07,171.1,71,'F',0.11,'V')
	cut.height = 208.4
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.04
	cut.height = 164.79
	cut.bodyfat = 0.13

def test_case_8():
	cut = calorie_intake_calc(113.92,167.61,59,'M',0.28,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_9():
	cut = calorie_intake_calc(87.1,166.19,51,'M',0.25,'E')
	cut.gender = 'N'
	cut.weight = 136.24
	result_determine_calorie_intake = cut.determine_calorie_intake()

