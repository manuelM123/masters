from cut import *

def test_case_0():
	cut = calorie_intake_calc(182.41,173.96,24,'M',0.25,'L')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(199.66,149.18,32,'F',0.3,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(180.17,213.25,63,'M',0.04,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.13

def test_case_3():
	cut = calorie_intake_calc(127.68,219.58,62,'N',0.04,'V')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 181.21

