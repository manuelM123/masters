from cut import *

def test_case_0():
	cut = calorie_intake_calc(170.84,198.5,32,'F',-0.31,'E')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 189.63

def test_case_1():
	cut = calorie_intake_calc(166.27,196.92,67,'F',0.72,'E')

def test_case_2():
	cut = calorie_intake_calc(70.62,181.86,18,'M',-0.02,'E')
	cut.weight = 101.72
	cut.age = 69
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(214.28,200.85,66,'F',0.7,'V')
	cut.bodyfat = -0.08

def test_case_4():
	cut = calorie_intake_calc(126.76,149.22,39,'N',0.26,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(152.19,200.98,84,'M',0.73,'E')
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'

