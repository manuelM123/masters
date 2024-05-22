from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	cut.gender = 'M'
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.age = 53
	cut.bodyfat = 0.16
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(151.03,153.56,75,'M',-0.29,'S')
	cut.weight = 93.38

def test_case_2():
	cut = calorie_intake_calc(184.34,144.5,5,'N',-0.08,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.57
	cut.bodyfat = 0.16
	cut.height = 203.78
	cut.weight = 128.03

def test_case_3():
	cut = calorie_intake_calc(157.95,205.75,19,'F',0.59,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.gender = 'M'
	cut.bodyfat = 0.76
	cut.weight = 86.55
	cut.age = 20
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.02

def test_case_4():
	cut = calorie_intake_calc(202.51,184.45,53,'M',0.77,'S')
	cut.bodyfat = -0.42
	cut.height = 152.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 150.19

def test_case_5():
	cut = calorie_intake_calc(205.12,217.45,67,'N',0.46,'V')
	cut.gender = 'F'
	cut.weight = 203.24
	cut.gender = 'F'
	cut.gender = 'F'
	cut.height = 156.82

def test_case_6():
	cut = calorie_intake_calc(91.11,193.36,71,'M',-0.19,'M')
	cut.gender = 'F'
	cut.age = 34
	cut.weight = 76.82
	cut.age = 63
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.13
	result_tdee_calculation = cut.tdee_calculation()

def test_case_7():
	cut = calorie_intake_calc(60.96,223.76,64,'F',0.26,'E')
	cut.age = 59
	cut.bodyfat = 0.12
	cut.bodyfat = -0.49

def test_case_8():
	cut = calorie_intake_calc(124.59,176.78,38,'F',-0.22,'L')

def test_case_9():
	cut = calorie_intake_calc(131.94,200.39,36,'F',-0.38,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 25
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.47

def test_case_10():
	cut = calorie_intake_calc(183.27,152.16,41,'F',-0.43,'S')
	cut.height = 189.39
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.bodyfat = 0.0

def test_case_11():
	cut = calorie_intake_calc(39.28,156.87,68,'M',-0.1,'V')
	cut.height = 138.3
	cut.amount_exercise = 'S'
	cut.age = 68
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 51
	cut.bodyfat = 0.71
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_12():
	cut = calorie_intake_calc(168.43,140.13,71,'M',-0.48,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_13():
	cut = calorie_intake_calc(151.1,217.95,21,'M',-0.0,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.weight = 177.39
	cut.height = 175.08
	result_tdee_calculation = cut.tdee_calculation()

def test_case_14():
	cut = calorie_intake_calc(98.19,206.17,48,'M',0.66,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 189.26
	cut.height = 143.15
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'V'
	cut.weight = 115.2
	cut.bodyfat = 0.14

def test_case_15():
	cut = calorie_intake_calc(165.65,191.67,75,'M',0.19,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 140.26
	cut.height = 184.68
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_16():
	cut = calorie_intake_calc(62.13,221.76,80,'N',0.68,'E')
	cut.height = 152.58
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 43
	cut.height = 210.25
	cut.bodyfat = 0.62

def test_case_17():
	cut = calorie_intake_calc(170.8,220.96,71,'F',-0.21,'L')
	cut.amount_exercise = 'L'
	cut.bodyfat = 0.1
	cut.weight = 177.7
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 211.25
	cut.amount_exercise = 'V'
	cut.age = 72
	cut.bodyfat = 0.69
	cut.gender = 'N'

def test_case_18():
	cut = calorie_intake_calc(138.67,147.1,44,'F',-0.26,'L')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 165.77

