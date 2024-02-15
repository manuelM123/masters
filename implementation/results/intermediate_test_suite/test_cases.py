from cut import *

def test_case_0():
	cut = calorie_intake_calc(40.32,162.27,44,'M',0.04,'S')
	cut.amount_exercise = 'S'

def test_case_1():
	cut = calorie_intake_calc(66.97,183.22,27,'F',0.07,'N')
	cut.age = 37
	cut.gender = 'F'
	cut.bodyfat = 0.11
	cut.bodyfat = 0.11

def test_case_2():
	cut = calorie_intake_calc(160.77,194.17,78,'M',0.26,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

