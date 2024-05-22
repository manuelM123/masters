from cut import *

def test_case_0():
	cut = calorie_intake_calc(208.3,140.21,83,'F',-0.09,'L')
	cut.bodyfat = 0.72

def test_case_1():
	cut = calorie_intake_calc(71.83,175.36,15,'M',0.12,'E')
	cut.height = 136.81
	cut.bodyfat = -0.38
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 46
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 35
	cut.weight = 53.16

def test_case_2():
	cut = calorie_intake_calc(150.16,163.35,74,'M',0.08,'V')
	cut.weight = 154.77
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 184.75
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'N'
	cut.height = 150.82
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(189.21,142.82,43,'M',-0.46,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'M'
	cut.weight = 103.5
	cut.weight = 146.31
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 116.08
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 176.9

def test_case_4():
	cut = calorie_intake_calc(53.49,155.0,54,'N',0.7,'L')

def test_case_5():
	cut = calorie_intake_calc(127.9,206.08,37,'N',0.52,'N')
	cut.weight = 90.62
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.12
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(61.36,148.17,20,'N',0.01,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 209.37
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 46.38
	cut.age = 64
	cut.amount_exercise = 'L'
	cut.weight = 90.88

def test_case_7():
	cut = calorie_intake_calc(105.33,136.24,19,'F',0.11,'M')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'

def test_case_8():
	cut = calorie_intake_calc(165.5,180.52,50,'F',-0.33,'E')
	cut.height = 186.21
	cut.height = 214.26
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

