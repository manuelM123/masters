from cut import *

def test_case_0():
	cut = calorie_intake_calc(44.71,180.95,72,'N',0.11,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(154.29,190.64,44,'F',0.22,'L')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(155.73,169.61,81,'N',0.06,'L')
	cut.weight = 70.09
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

