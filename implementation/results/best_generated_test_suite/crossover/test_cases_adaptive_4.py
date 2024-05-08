from cut import *

def test_case_0():
	cut = calorie_intake_calc(88.74,189.09,25,'F',0.03,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.31

def test_case_1():
	cut = calorie_intake_calc(195.6,172.2,16,'N',0.16,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 151.54

