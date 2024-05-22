from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.39,157.64,80,'F',0.15,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	cut.bodyfat = 0.08
	cut.gender = 'M'
	cut.weight = 112.48

def test_case_1():
	cut = calorie_intake_calc(123.05,139.27,37,'N',0.42,'L')
	cut.age = 51

def test_case_2():
	cut = calorie_intake_calc(94.57,179.82,25,'M',-0.35,'M')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 72
	cut.amount_exercise = 'N'

