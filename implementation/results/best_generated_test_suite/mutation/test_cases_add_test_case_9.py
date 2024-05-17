from cut import *

def test_case_0():
	cut = calorie_intake_calc(42.25,149.0,82,'F',-0.46,'S')
	cut.bodyfat = -0.02
	cut.weight = 177.93
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(157.04,162.52,47,'F',-0.26,'E')
	cut.age = 13
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(79.2,191.17,42,'N',-0.26,'E')
	cut.amount_exercise = 'S'

def test_case_3():
	cut = calorie_intake_calc(96.24,175.33,50,'M',0.63,'L')
	cut.height = 183.3
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()

