from cut import *

def test_case_0():
	cut = calorie_intake_calc(135.91,181.82,28,'N',0.15,'N')
	cut.height = 182.19
	cut.gender = 'M'
	cut.height = 172.24
	cut.amount_exercise = 'S'

def test_case_1():
	cut = calorie_intake_calc(139.26,154.27,27,'N',0.06,'S')

