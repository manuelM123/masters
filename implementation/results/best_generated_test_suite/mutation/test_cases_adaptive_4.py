from cut import *

def test_case_0():
	cut = calorie_intake_calc(116.4,200.06,74,'N',0.14,'L')
	cut.gender = 'M'
	cut.height = 142.27

def test_case_1():
	cut = calorie_intake_calc(100.47,164.03,28,'F',0.08,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(57.53,192.05,43,'M',0.21,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.bodyfat = 0.12

