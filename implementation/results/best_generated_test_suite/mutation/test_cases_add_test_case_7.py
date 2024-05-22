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
	cut = calorie_intake_calc(74.62,204.43,65,'F',-0.32,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

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
	cut = calorie_intake_calc(91.03,219.41,16,'M',0.8,'N')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(205.12,217.45,67,'N',0.46,'V')
	cut.gender = 'F'
	cut.weight = 203.24
	cut.gender = 'F'
	cut.gender = 'F'
	cut.height = 156.82

def test_case_6():
	cut = calorie_intake_calc(126.46,139.76,11,'N',0.17,'M')
	cut.gender = 'F'
	cut.age = 83

def test_case_7():
	cut = calorie_intake_calc(78.78,141.52,58,'F',0.25,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 57.16
	cut.age = 65
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 223.89
	result_tdee_calculation = cut.tdee_calculation()

def test_case_8():
	cut = calorie_intake_calc(36.6,190.76,70,'M',0.22,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 142.22

def test_case_9():
	cut = calorie_intake_calc(155.88,156.84,50,'F',-0.2,'S')
	cut.height = 164.8
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.46

def test_case_10():
	cut = calorie_intake_calc(145.41,224.83,23,'F',-0.33,'L')
	cut.weight = 146.7
	cut.height = 150.64
	result_tdee_calculation = cut.tdee_calculation()

def test_case_11():
	cut = calorie_intake_calc(82.66,197.39,6,'M',0.7,'V')
	cut.height = 182.23

def test_case_12():
	cut = calorie_intake_calc(197.65,215.25,69,'M',0.15,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.39
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 188.94
	cut.gender = 'M'
	cut.age = 7
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'M'

def test_case_13():
	cut = calorie_intake_calc(130.63,191.92,45,'N',0.72,'V')
	cut.amount_exercise = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 185.44
	cut.weight = 36.35
	cut.age = 43
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'
	cut.bodyfat = 0.43
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_14():
	cut = calorie_intake_calc(164.53,157.41,77,'F',-0.2,'N')
	cut.age = 52
	cut.height = 152.59
	cut.gender = 'M'
	cut.age = 42
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'S'
	cut.age = 55
	cut.bodyfat = 0.56
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 51.65

