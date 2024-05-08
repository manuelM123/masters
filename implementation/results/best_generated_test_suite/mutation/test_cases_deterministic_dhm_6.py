from cut import *

def test_case_0():
	cut = calorie_intake_calc(42.44,149.71,45,'F',0.3,'L')
	cut.weight = 180.71
	cut.weight = 199.13
	cut.height = 156.85
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(84.02,221.28,54,'M',0.48,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 9
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.39
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(172.12,179.11,40,'F',-0.2,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 195.81
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.16
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_3():
	cut = calorie_intake_calc(189.49,149.47,80,'M',-0.1,'M')
	cut.amount_exercise = 'M'
	cut.bodyfat = 0.03
	cut.gender = 'M'
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.28
	cut.height = 171.74
	cut.gender = 'M'

