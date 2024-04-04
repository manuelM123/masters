from cut import *

def test_case_0():
	cut = calorie_intake_calc(67.88,187.86,20,'M',0.06,'V')
	cut.weight = 143.57
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 206.61
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(45.95,199.9,19,'F',0.07,'E')
	cut.weight = 102.98
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(144.95,208.31,36,'M',0.0,'M')
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 18
	result_tdee_calculation = cut.tdee_calculation()

