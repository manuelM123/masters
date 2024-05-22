from cut import *

def test_case_0():
	cut = calorie_intake_calc(77.33,184.83,70,'M',-0.19,'L')
	cut.height = 175.72
	cut.weight = 91.44
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'L'
	cut.age = 53
	cut.bodyfat = 0.23
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(50.39,181.03,57,'F',0.69,'S')
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(184.34,144.5,5,'N',-0.08,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 191.6
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(140.19,195.56,73,'M',0.09,'V')
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 198.98
	cut.age = 28
	cut.gender = 'M'
	cut.weight = 138.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(209.8,164.3,65,'F',-0.45,'L')
	cut.amount_exercise = 'E'
	cut.age = 11
	cut.age = 48
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'F'
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

