from cut import *

def test_case_0():
	cut = calorie_intake_calc(135.91,181.82,28,'N',0.15,'N')
	cut.height = 182.19
	cut.gender = 'M'
	cut.height = 172.24
	cut.amount_exercise = 'S'

def test_case_1():
	cut = calorie_intake_calc(54.85,204.54,36,'N',0.2,'M')

def test_case_2():
	cut = calorie_intake_calc(134.17,201.35,13,'M',0.18,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.15

