from cut import *

def test_case_0():
	cut = calorie_intake_calc(185.45,199.19,28,'M',0.23,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(41.33,183.79,20,'N',0.25,'N')
	cut.gender = 'M'

def test_case_2():
	cut = calorie_intake_calc(168.1,214.29,24,'M',0.15,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

