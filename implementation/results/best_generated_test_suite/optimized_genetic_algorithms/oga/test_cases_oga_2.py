from cut import *

def test_case_0():
	cut = calorie_intake_calc(181.34,155.69,20,'F',0.56,'E')

def test_case_1():
	cut = calorie_intake_calc(172.37,202.38,36,'M',0.23,'M')
	cut.gender = 'N'

