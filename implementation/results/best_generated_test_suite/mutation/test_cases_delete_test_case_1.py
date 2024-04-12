from cut import *

def test_case_0():
	cut = calorie_intake_calc(47.43,151.71,54,'M',0.06,'S')
	cut.gender = 'N'
	cut.gender = 'M'
	cut.bodyfat = 0.22

def test_case_1():
	cut = calorie_intake_calc(98.11,201.74,57,'F',0.18,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 105.04
	cut.age = 17
	cut.age = 81
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_2():
	cut = calorie_intake_calc(98.85,192.74,26,'M',0.26,'L')
	cut.weight = 60.92
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.06
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()

