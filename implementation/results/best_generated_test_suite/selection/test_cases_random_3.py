from cut import *

def test_case_0():
	cut = calorie_intake_calc(161.56,220.98,68,'N',0.72,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_1():
	cut = calorie_intake_calc(181.79,141.08,32,'F',-0.09,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 85
	cut.weight = 209.48
	cut.bodyfat = 0.36
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 156.26

def test_case_2():
	cut = calorie_intake_calc(78.93,147.66,60,'F',0.72,'M')
	cut.bodyfat = -0.15
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(154.55,186.49,77,'F',-0.22,'S')
	cut.bodyfat = -0.31
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 78
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 139.54
	cut.weight = 77.01

def test_case_4():
	cut = calorie_intake_calc(71.49,171.8,71,'M',-0.14,'E')
	cut.bodyfat = -0.18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	cut.weight = 104.37
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 186.76
	cut.gender = 'F'
	cut.bodyfat = -0.33

