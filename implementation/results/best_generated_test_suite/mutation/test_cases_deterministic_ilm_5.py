from cut import *

def test_case_0():
	cut = calorie_intake_calc(118.18,209.29,81,'F',-0.14,'M')
	cut.height = 199.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(79.29,202.47,73,'M',-0.28,'E')
	cut.weight = 45.01
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 28
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.01
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

