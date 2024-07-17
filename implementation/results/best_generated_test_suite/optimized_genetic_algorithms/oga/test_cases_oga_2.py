from cut import *

def test_case_0():
	cut = calorie_intake_calc(178.41,191.77,22,'F',-0.1,'E')

def test_case_1():
	cut = calorie_intake_calc(67.69,141.52,22,'F',-0.11,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.19
	cut.height = 155.34

def test_case_2():
	cut = calorie_intake_calc(154.55,175.8,35,'M',0.03,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 201.73

def test_case_3():
	cut = calorie_intake_calc(171.05,178.11,13,'F',0.23,'L')
	cut.height = 166.29
	cut.weight = 213.71
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

