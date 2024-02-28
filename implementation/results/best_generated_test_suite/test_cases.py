from cut import *

def test_case_0():
	cut = calorie_intake_calc(174.75,207.93,76,'M',0.26,'S')
	cut.amount_exercise = 'L'

def test_case_1():
	cut = calorie_intake_calc(133.44,175.19,42,'F',0.0,'E')
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(191.37,197.51,49,'M',0.16,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(45.15,174.72,58,'M',0.06,'E')

