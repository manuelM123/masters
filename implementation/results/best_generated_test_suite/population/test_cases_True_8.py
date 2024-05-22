from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.66,156.43,14,'N',-0.47,'M')

def test_case_1():
	cut = calorie_intake_calc(128.21,161.78,63,'M',0.14,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 216.73
	cut.weight = 136.34
	cut.bodyfat = -0.36
	cut.bodyfat = 0.12
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 203.86

def test_case_2():
	cut = calorie_intake_calc(159.66,158.18,13,'M',0.19,'V')
	cut.bodyfat = -0.09
	cut.weight = 203.04
	cut.weight = 161.7
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 32
	cut.weight = 84.21
	cut.weight = 51.12
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 18
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(183.43,173.03,52,'F',-0.42,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.gender = 'N'

def test_case_4():
	cut = calorie_intake_calc(212.51,170.34,35,'F',0.5,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 109.55

def test_case_5():
	cut = calorie_intake_calc(181.28,210.08,84,'N',0.07,'L')
	cut.gender = 'F'
	cut.height = 158.0
	cut.height = 185.15
	cut.age = 74
	cut.height = 139.5
	cut.age = 17
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(119.02,179.26,11,'N',0.7,'S')
	cut.age = 64
	cut.age = 15
	cut.height = 162.97
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 185.58
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(86.32,223.24,23,'N',0.02,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 128.57
	cut.height = 175.44

def test_case_8():
	cut = calorie_intake_calc(141.79,220.35,78,'M',-0.49,'L')
	cut.gender = 'N'

def test_case_9():
	cut = calorie_intake_calc(100.85,206.7,12,'F',-0.03,'V')
	cut.weight = 96.15
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 176.94
	cut.bodyfat = 0.53

