from cut import *

def test_case_0():
	cut = calorie_intake_calc(58.62,210.22,30,'M',0.72,'N')
	cut.weight = 150.24
	cut.amount_exercise = 'S'
	cut.bodyfat = -0.08
	cut.weight = 187.35
	cut.amount_exercise = 'M'

def test_case_1():
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(204.4,205.91,25,'F',0.43,'L')
	cut.amount_exercise = 'E'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 167.48
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(136.03,181.95,34,'M',0.25,'S')
	cut.height = 205.56
	cut.amount_exercise = 'M'
	cut.bodyfat = -0.28
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 42.61
	cut.weight = 108.68

def test_case_4():
	cut = calorie_intake_calc(84.6,178.7,21,'M',-0.47,'L')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.age = 23
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 121.78
	cut.amount_exercise = 'S'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(171.95,141.93,77,'N',0.67,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46
	cut.amount_exercise = 'L'
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 200.04
	cut.gender = 'F'

def test_case_6():
	cut = calorie_intake_calc(184.09,170.18,8,'F',0.65,'N')
	cut.gender = 'M'
	cut.age = 79
	cut.gender = 'F'
	cut.height = 154.86

def test_case_7():
	cut = calorie_intake_calc(44.64,220.84,26,'F',0.54,'E')
	cut.bodyfat = 0.58
	cut.gender = 'M'
	cut.height = 202.82
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.age = 68
	cut.height = 164.32
	cut.height = 147.88
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'

def test_case_8():
	cut = calorie_intake_calc(81.98,206.96,76,'N',0.5,'L')
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.18
	cut.weight = 107.93

def test_case_9():
	cut = calorie_intake_calc(71.38,196.21,66,'N',0.08,'S')
	cut.age = 23
	cut.weight = 183.31

def test_case_10():
	cut = calorie_intake_calc(131.65,215.02,71,'M',-0.09,'N')
	cut.age = 50
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_11():
	cut = calorie_intake_calc(187.24,209.7,67,'M',-0.23,'M')
	cut.bodyfat = -0.34
	cut.weight = 38.78

def test_case_12():
	cut = calorie_intake_calc(43.06,172.57,68,'F',-0.32,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.3
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 85.06
	cut.amount_exercise = 'E'
	cut.age = 51
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.14
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 36.47

def test_case_13():
	cut = calorie_intake_calc(40.71,192.13,61,'N',-0.39,'E')
	cut.age = 71
	cut.weight = 193.14
	cut.height = 212.43
	cut.gender = 'M'
	cut.age = 58
	cut.amount_exercise = 'E'
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_14():
	cut = calorie_intake_calc(185.81,197.78,48,'F',0.12,'V')
	cut.bodyfat = -0.41
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 39
	cut.weight = 138.18
	result_tdee_calculation = cut.tdee_calculation()

def test_case_15():
	cut = calorie_intake_calc(51.16,138.43,69,'F',0.45,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 68
	cut.gender = 'N'
	cut.age = 19
	cut.weight = 105.5

