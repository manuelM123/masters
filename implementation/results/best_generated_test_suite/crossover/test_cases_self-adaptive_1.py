from cut import *

def test_case_0():
	cut = calorie_intake_calc(114.85,188.62,26,'M',0.11,'N')
	cut.age = 26

def test_case_1():
	cut = calorie_intake_calc(119.3,187.2,11,'N',0.13,'N')
	cut.age = 24
	cut.bodyfat = 0.14
	cut.height = 195.73

def test_case_2():
	cut = calorie_intake_calc(187.74,168.51,60,'F',0.2,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 173.84

