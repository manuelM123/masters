from cut import *

def test_case_0():
	cut = calorie_intake_calc(105.96,151.54,38,'M',0.21,'E')

def test_case_1():
	cut = calorie_intake_calc(141.79,148.97,46,'M',0.1,'N')
	cut.gender = 'F'

def test_case_2():
	cut = calorie_intake_calc(103.53,200.63,17,'N',0.25,'S')
	cut.gender = 'F'

