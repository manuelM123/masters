from cut import *

def test_case_0():
	cut = calorie_intake_calc(144.85,219.01,41,'F',0.28,'E')
	cut.height = 158.7
	cut.bodyfat = 0.18

def test_case_1():
	cut = calorie_intake_calc(118.7,161.37,38,'N',0.05,'S')
	cut.gender = 'M'
	cut.height = 153.43

def test_case_2():
	cut = calorie_intake_calc(175.09,220.59,21,'F',0.27,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'L'

def test_case_3():
	cut = calorie_intake_calc(145.91,154.95,71,'N',0.27,'L')
	cut.bodyfat = 0.18
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(103.69,219.8,34,'F',0.15,'M')
	result_tdee_calculation = cut.tdee_calculation()

