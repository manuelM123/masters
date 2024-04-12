from cut import *

def test_case_0():
	cut = calorie_intake_calc(114.41,190.07,41,'N',0.1,'M')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_1():
	cut = calorie_intake_calc(121.29,186.7,79,'M',0.24,'S')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	cut.age = 13
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 38
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'N'

