from cut import *

def test_case_0():
	cut = calorie_intake_calc(68.45,216.61,25,'N',0.2,'L')
	cut.amount_exercise = 'E'
	cut.gender = 'F'
	cut.amount_exercise = 'L'
	cut.gender = 'M'

def test_case_1():
	cut = calorie_intake_calc(157.99,158.5,10,'N',0.21,'V')

