from cut import *

def test_case_0():
	cut = calorie_intake_calc(94.42,154.99,40,'F',0.24,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.15
	cut.amount_exercise = 'M'
	cut.height = 142.12
	cut.bodyfat = 0.02
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(88.92,208.49,80,'M',0.15,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 118.91
	cut.height = 159.79
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 140.52
	cut.weight = 129.36

def test_case_2():
	cut = calorie_intake_calc(133.84,192.97,63,'M',0.07,'N')
	cut.age = 29
	cut.weight = 56.06
	cut.age = 19
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.height = 181.59
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_3():
	cut = calorie_intake_calc(91.89,177.27,26,'M',0.08,'E')
	cut.height = 210.7
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 159.06
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

