from cut import *

def test_case_0():
	cut = calorie_intake_calc(148.6,218.62,81,'N',-0.3,'L')
	cut.weight = 89.44
	cut.age = 17
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(177.19,209.01,67,'N',0.51,'S')
	cut.height = 157.51
	cut.height = 137.59
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(135.52,166.06,39,'M',-0.17,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 202.24

def test_case_3():
	cut = calorie_intake_calc(164.15,151.89,11,'M',0.03,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.2
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 6

