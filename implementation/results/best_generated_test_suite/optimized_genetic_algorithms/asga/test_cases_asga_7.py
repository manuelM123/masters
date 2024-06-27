from cut import *

def test_case_0():
	cut = calorie_intake_calc(130.6,137.18,63,'F',0.03,'N')
	cut.bodyfat = 0.77
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(210.71,143.44,42,'F',-0.03,'N')
	cut.bodyfat = 0.42
	cut.height = 198.46
	cut.bodyfat = -0.43
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(192.74,182.23,74,'F',0.11,'L')
	cut.weight = 143.7
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(146.43,210.96,25,'M',-0.23,'E')
	cut.height = 205.58
	result_determine_calorie_intake = cut.determine_calorie_intake()

