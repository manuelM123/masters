from cut import *

def test_case_0():
	cut = calorie_intake_calc(70.27,181.14,66,'N',0.04,'V')

def test_case_1():
	cut = calorie_intake_calc(137.89,165.36,45,'F',0.03,'M')
	cut.gender = 'M'
	cut.age = 28

def test_case_2():
	cut = calorie_intake_calc(138.01,183.9,25,'F',0.15,'S')
	cut.amount_exercise = 'S'
	cut.height = 172.55
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(72.27,196.15,65,'F',0.26,'E')
	cut.weight = 68.17
	cut.weight = 110.47
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'

