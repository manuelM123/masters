from cut import *

def test_case_0():
	cut = calorie_intake_calc(190.74,145.11,19,'M',0.01,'S')
	cut.height = 175.85
	cut.weight = 64.3
	cut.bodyfat = 0.45
	cut.bodyfat = 0.51
	cut.height = 150.77
	cut.bodyfat = -0.4
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(44.57,147.18,58,'F',-0.47,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

