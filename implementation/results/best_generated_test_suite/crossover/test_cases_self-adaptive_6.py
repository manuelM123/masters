from cut import *

def test_case_0():
	cut = calorie_intake_calc(173.22,215.24,62,'F',-0.3,'V')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(211.72,214.2,73,'N',0.02,'E')
	cut.age = 12
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	cut.height = 175.79
	cut.weight = 159.61

def test_case_2():
	cut = calorie_intake_calc(146.48,197.48,17,'N',-0.22,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 100.63
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 208.21
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 25
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.16

def test_case_3():
	cut = calorie_intake_calc(43.69,137.2,33,'F',-0.12,'E')
	cut.age = 18
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.78
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(84.38,159.72,15,'F',-0.13,'E')
	cut.age = 11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_5():
	cut = calorie_intake_calc(192.32,180.56,36,'F',0.43,'S')
	cut.bodyfat = 0.19
	cut.age = 24
	cut.bodyfat = 0.51
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 184.95
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_6():
	cut = calorie_intake_calc(142.94,173.61,34,'F',-0.43,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'E'
	cut.height = 212.25
	cut.amount_exercise = 'E'
	cut.gender = 'M'
	cut.bodyfat = 0.53

def test_case_7():
	cut = calorie_intake_calc(120.1,179.12,7,'M',0.28,'S')

