from cut import *

def test_case_0():
	cut = calorie_intake_calc(183.74,218.11,57,'F',0.06,'N')
	cut.height = 205.49
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(200.81,154.2,16,'N',0.17,'V')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 140.59

def test_case_2():
	cut = calorie_intake_calc(81.23,175.14,27,'N',0.2,'M')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(63.77,156.08,75,'M',0.12,'V')
	cut.height = 165.79
	cut.amount_exercise = 'E'

