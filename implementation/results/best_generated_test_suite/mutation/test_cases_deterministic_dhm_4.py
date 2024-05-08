from cut import *

def test_case_0():
	cut = calorie_intake_calc(183.44,136.31,9,'M',-0.16,'M')
	cut.age = 58
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 114.9
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(173.81,224.32,45,'N',-0.34,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(73.05,178.89,21,'M',-0.2,'V')
	cut.height = 200.21
	cut.gender = 'M'
	cut.bodyfat = 0.47
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(167.84,203.2,16,'M',-0.06,'V')
	cut.amount_exercise = 'E'
	cut.age = 20
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 61
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(128.81,141.86,81,'M',0.74,'E')
	cut.age = 74

