from cut import *

def test_case_0():
	cut = calorie_intake_calc(170.16,185.33,38,'F',0.41,'E')
	cut.weight = 40.86
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 212.1

def test_case_1():
	cut = calorie_intake_calc(47.73,163.22,41,'M',0.08,'V')
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(142.69,157.03,66,'M',-0.23,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.21
	cut.height = 138.75

def test_case_3():
	cut = calorie_intake_calc(88.77,154.84,23,'F',0.3,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

