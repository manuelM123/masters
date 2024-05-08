from cut import *

def test_case_0():
	cut = calorie_intake_calc(139.46,222.83,85,'N',-0.47,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 71
	cut.age = 17
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(150.17,191.32,36,'F',-0.32,'M')
	cut.bodyfat = -0.04
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'M'
	cut.weight = 106.09
	cut.amount_exercise = 'V'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 182.82
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(170.05,193.76,49,'N',0.0,'E')
	cut.age = 19
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 193.43
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 213.4
	cut.weight = 179.55

def test_case_3():
	cut = calorie_intake_calc(133.29,211.63,55,'M',-0.08,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.age = 26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.24
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 25
	cut.height = 193.92
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.4
	cut.weight = 39.29

