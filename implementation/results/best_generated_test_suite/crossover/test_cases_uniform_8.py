from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	cut.height = 206.13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.56
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.08
	cut.amount_exercise = 'S'
	cut.age = 22

def test_case_1():
	cut = calorie_intake_calc(101.63,205.16,19,'F',-0.46,'S')
	cut.weight = 130.52

def test_case_2():
	cut = calorie_intake_calc(71.87,178.85,36,'M',-0.33,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 162.77
	cut.age = 44
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.age = 15
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.19
	cut.gender = 'N'

