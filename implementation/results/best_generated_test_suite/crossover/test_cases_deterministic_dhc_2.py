from cut import *

def test_case_0():
	cut = calorie_intake_calc(81.44,176.78,81,'N',-0.49,'L')
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 140.83
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(130.75,145.57,63,'F',-0.16,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 87.61
	cut.gender = 'F'
	cut.age = 20
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.13
	cut.bodyfat = 0.32
	cut.age = 13

