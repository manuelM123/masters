from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	cut.gender = 'F'
	cut.weight = 194.75
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 151.11
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 69
	cut.age = 22

def test_case_1():
	cut = calorie_intake_calc(160.92,156.65,39,'M',0.63,'L')
	cut.bodyfat = 0.5
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'E'
	cut.age = 49
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(71.87,178.85,36,'M',-0.33,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 171.14
	cut.age = 15
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 55

def test_case_3():
	cut = calorie_intake_calc(190.26,193.52,48,'N',0.23,'M')
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 220.0
	cut.height = 207.4

def test_case_4():
	cut = calorie_intake_calc(212.42,216.62,77,'M',-0.22,'M')

def test_case_5():
	cut = calorie_intake_calc(73.3,169.88,5,'F',0.47,'L')
	cut.weight = 39.98

