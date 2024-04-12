from cut import *

def test_case_0():
	cut = calorie_intake_calc(154.94,220.58,62,'M',0.27,'E')
	cut.weight = 46.01
	cut.height = 180.76
	cut.age = 44
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.1
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 199.29

def test_case_1():
	cut = calorie_intake_calc(143.63,152.19,57,'M',0.29,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.06
	cut.age = 25
	cut.weight = 68.31
	cut.height = 188.46
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(74.06,142.15,67,'F',0.01,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(161.17,145.31,56,'F',0.27,'S')
	cut.amount_exercise = 'L'
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	cut.amount_exercise = 'S'
	cut.gender = 'M'

