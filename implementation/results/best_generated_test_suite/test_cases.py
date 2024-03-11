from cut import *

def test_case_0():
	cut = calorie_intake_calc(170.97,218.42,73,'N',0.18,'M')
	cut.age = 73

def test_case_1():
	cut = calorie_intake_calc(157.99,158.5,10,'N',0.21,'V')

