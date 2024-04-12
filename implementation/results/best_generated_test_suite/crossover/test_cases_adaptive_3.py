from cut import *

def test_case_0():
	cut = calorie_intake_calc(138.8,220.86,44,'M',0.01,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 153.59
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(178.11,178.37,69,'M',0.0,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 162.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 141.21
	cut.gender = 'N'
	cut.weight = 118.14
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 125.83
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(134.39,179.57,16,'M',0.08,'N')

def test_case_3():
	cut = calorie_intake_calc(57.41,149.04,11,'M',0.1,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.03
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.04
	cut.bodyfat = 0.27

