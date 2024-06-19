from cut import *

def test_case_0():
	cut = calorie_intake_calc(158.49,206.73,56,'F',0.04,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(147.8,193.43,11,'M',-0.02,'M')

