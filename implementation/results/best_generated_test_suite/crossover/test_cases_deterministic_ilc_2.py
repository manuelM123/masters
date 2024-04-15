from cut import *

def test_case_0():
	cut = calorie_intake_calc(154.0,184.77,42,'N',0.18,'M')

def test_case_1():
	cut = calorie_intake_calc(111.89,152.85,65,'F',0.22,'E')
	cut.bodyfat = 0.05
	cut.height = 140.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(138.01,183.9,25,'F',0.15,'S')
	cut.amount_exercise = 'S'
	cut.height = 172.55
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

