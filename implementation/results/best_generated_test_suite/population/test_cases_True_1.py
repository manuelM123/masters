from cut import *

def test_case_0():
	cut = calorie_intake_calc(85.99,141.1,15,'M',0.11,'N')

def test_case_1():
	cut = calorie_intake_calc(128.89,220.08,76,'N',0.12,'L')
	cut.age = 38
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(186.16,154.34,64,'M',0.13,'E')

