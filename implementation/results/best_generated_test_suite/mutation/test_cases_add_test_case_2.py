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
	cut = calorie_intake_calc(129.39,200.26,44,'F',0.3,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.53
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(184.34,144.5,5,'N',-0.08,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.57
	cut.bodyfat = 0.16
	cut.height = 203.78
	cut.weight = 128.03

def test_case_3():
	cut = calorie_intake_calc(175.06,136.42,77,'N',-0.47,'N')
	cut.weight = 35.68
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'M'
	cut.weight = 189.81
	cut.age = 76
	cut.gender = 'F'

def test_case_4():
	cut = calorie_intake_calc(195.1,161.02,47,'M',0.37,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 61
	cut.gender = 'N'
	cut.gender = 'M'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_5():
	cut = calorie_intake_calc(66.18,183.31,50,'F',0.06,'N')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.age = 6
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 65.72
	cut.height = 206.4
	cut.height = 154.6
	cut.bodyfat = -0.23

def test_case_6():
	cut = calorie_intake_calc(122.32,159.01,60,'N',0.14,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 53
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.11
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(35.93,160.94,26,'N',-0.39,'M')
	cut.age = 78
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.73
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_8():
	cut = calorie_intake_calc(42.81,157.6,30,'M',0.07,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	cut.bodyfat = 0.47
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = 0.29
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

def test_case_9():
	cut = calorie_intake_calc(181.11,149.33,72,'F',-0.01,'S')
	cut.weight = 73.23
	cut.amount_exercise = 'M'
	cut.bodyfat = -0.3
	cut.weight = 165.7
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.31
	result_tdee_calculation = cut.tdee_calculation()

def test_case_10():
	cut = calorie_intake_calc(103.56,215.12,31,'F',0.19,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 50.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 101.14
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

