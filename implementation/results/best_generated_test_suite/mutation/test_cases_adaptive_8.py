from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.11
	cut.gender = 'N'
	cut.gender = 'M'
	cut.age = 69
	cut.weight = 202.93

def test_case_1():
	cut = calorie_intake_calc(129.39,200.26,44,'F',0.3,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 57
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(71.87,178.85,36,'M',-0.33,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 162.77
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 171.14
	cut.age = 15
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.19
	cut.amount_exercise = 'N'

def test_case_3():
	cut = calorie_intake_calc(82.59,219.48,52,'F',-0.0,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 78
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(167.7,151.55,58,'M',0.74,'S')
	cut.age = 44
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'S'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

