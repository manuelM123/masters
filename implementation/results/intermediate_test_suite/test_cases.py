from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.75,193.2,67,'N',0.28,'M')
	cut.bodyfat = 0.12

def test_case_1():
	cut = calorie_intake_calc(109.59,162.04,59,'F',0.22,'N')
	cut.weight = 133.22
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(125.36,161.25,30,'N',0.11,'E')
	cut.height = 157.24
	cut.age = 58
	cut.amount_exercise = 'L'

def test_case_3():
	cut = calorie_intake_calc(123.52,192.13,33,'F',0.23,'E')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(135.02,172.9,18,'F',0.26,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(155.45,191.74,45,'M',0.28,'L')

