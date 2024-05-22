from cut import *

def test_case_0():
	cut = calorie_intake_calc(45.48,156.24,35,'M',-0.48,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'
	cut.weight = 50.0
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.66
	cut.height = 223.42
	cut.height = 214.18

def test_case_1():
	cut = calorie_intake_calc(65.23,179.58,27,'M',0.73,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 137.37
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_2():
	cut = calorie_intake_calc(122.29,178.52,69,'N',-0.28,'L')
	cut.age = 20
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 153.27

def test_case_3():
	cut = calorie_intake_calc(172.52,195.47,33,'M',0.77,'V')
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'E'
	cut.height = 191.21
	cut.age = 52

def test_case_4():
	cut = calorie_intake_calc(202.55,160.32,42,'M',-0.19,'V')
	cut.age = 44
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.2

def test_case_5():
	cut = calorie_intake_calc(123.33,213.95,63,'M',0.47,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.47
	cut.gender = 'F'

def test_case_6():
	cut = calorie_intake_calc(175.73,201.42,61,'M',0.21,'M')
	cut.weight = 200.89
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 95.9
	cut.bodyfat = 0.27
	cut.weight = 183.91

