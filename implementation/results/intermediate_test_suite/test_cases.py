from cut import *

def test_case_0():
	cut = calorie_intake_calc(187.0,153.54,13,'M',0.27,'N')
	cut.weight = 149.34

def test_case_1():
	cut = calorie_intake_calc(135.19,213.11,65,'F',0.09,'L')
	cut.amount_exercise = 'S'
	cut.height = 194.16

