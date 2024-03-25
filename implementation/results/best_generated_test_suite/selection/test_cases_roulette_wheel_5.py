from cut import *

def test_case_0():
	cut = calorie_intake_calc(177.13,200.42,77,'F',0.2,'V')
	cut.bodyfat = 0.02
	cut.weight = 92.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.weight = 210.07
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.3
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(73.08,212.34,62,'F',0.3,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	cut.weight = 83.7
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(53.6,198.67,23,'N',0.15,'E')
	cut.amount_exercise = 'N'
	cut.weight = 190.47
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 192.3
	cut.bodyfat = 0.11

def test_case_3():
	cut = calorie_intake_calc(135.32,174.52,21,'M',0.04,'M')
	cut.height = 203.11
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(68.84,198.53,10,'M',0.18,'E')
	cut.bodyfat = 0.01
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'

