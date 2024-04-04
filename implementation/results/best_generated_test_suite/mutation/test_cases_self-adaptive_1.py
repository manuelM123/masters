from cut import *

def test_case_0():
	cut = calorie_intake_calc(205.65,152.91,54,'M',0.26,'S')
	cut.height = 213.78
	cut.weight = 93.85
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(47.84,146.32,57,'M',0.26,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(168.02,212.47,17,'F',0.2,'E')
	cut.weight = 122.81
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 45
	result_tdee_calculation = cut.tdee_calculation()

