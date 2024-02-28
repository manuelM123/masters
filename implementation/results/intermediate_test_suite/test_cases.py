from cut import *

def test_case_0():
	cut = calorie_intake_calc(134.28,157.51,20,'M',0.21,'L')

def test_case_1():
	cut = calorie_intake_calc(194.04,202.37,47,'N',0.18,'N')

def test_case_2():
	cut = calorie_intake_calc(90.67,203.64,13,'F',0.27,'N')
	cut.weight = 86.42

def test_case_3():
	cut = calorie_intake_calc(159.65,152.36,43,'F',0.12,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

