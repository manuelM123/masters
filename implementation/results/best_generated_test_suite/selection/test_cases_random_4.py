from cut import *

def test_case_0():
	cut = calorie_intake_calc(188.64,146.93,69,'F',0.18,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'L'
	cut.weight = 133.72

def test_case_1():
	cut = calorie_intake_calc(67.79,178.59,28,'N',0.44,'M')
	cut.gender = 'F'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 142.1

def test_case_2():
	cut = calorie_intake_calc(204.4,205.91,25,'F',0.43,'L')
	cut.amount_exercise = 'E'
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 167.48
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(169.22,142.88,18,'N',-0.28,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 81
	cut.height = 187.07
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'

def test_case_4():
	cut = calorie_intake_calc(112.12,153.12,40,'M',-0.21,'L')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 200.06
	cut.gender = 'N'
	cut.height = 168.32
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(54.57,202.46,16,'N',-0.24,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	cut.age = 38
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 139.9

def test_case_6():
	cut = calorie_intake_calc(58.61,196.52,7,'N',0.38,'M')
	cut.weight = 209.25
	cut.height = 136.39
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 46
	cut.bodyfat = -0.34

def test_case_7():
	cut = calorie_intake_calc(81.7,215.28,10,'M',0.45,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 68
	cut.amount_exercise = 'S'
	cut.height = 192.05
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_8():
	cut = calorie_intake_calc(37.18,172.9,66,'M',0.35,'S')
	cut.age = 51
	cut.bodyfat = -0.4
	cut.age = 74
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 185.67

def test_case_9():
	cut = calorie_intake_calc(36.29,157.49,69,'M',0.63,'E')
	cut.height = 214.75
	cut.amount_exercise = 'E'
	cut.bodyfat = 0.31
	cut.weight = 48.01
	cut.gender = 'F'
	cut.bodyfat = 0.52

