from cut import *

def test_case_0():
	cut = calorie_intake_calc(181.6,155.99,47,'M',-0.13,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 69
	cut.weight = 69.37

def test_case_1():
	cut = calorie_intake_calc(66.99,195.36,31,'M',-0.03,'E')

