from cut import *

def test_case_0():
	cut = calorie_intake_calc(151.64,208.69,50,'F',0.02,'E')
	cut.amount_exercise = 'V'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'F'
	cut.age = 32

def test_case_1():
	cut = calorie_intake_calc(55.41,186.43,68,'F',0.31,'M')
	cut.amount_exercise = 'S'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'L'
	cut.gender = 'N'

def test_case_2():
	cut = calorie_intake_calc(131.51,176.05,45,'N',-0.11,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 160.45
	cut.gender = 'M'

def test_case_3():
	cut = calorie_intake_calc(126.39,173.42,47,'M',-0.26,'L')
	cut.amount_exercise = 'E'
	cut.weight = 99.63
	cut.height = 198.9
	cut.age = 47
	cut.weight = 140.86
	cut.bodyfat = -0.46
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_4():
	cut = calorie_intake_calc(145.46,194.96,46,'N',0.37,'N')
	cut.gender = 'N'
	cut.bodyfat = -0.49
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'
	cut.bodyfat = 0.01
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 168.89

def test_case_5():
	cut = calorie_intake_calc(45.12,223.81,67,'F',0.42,'N')
	cut.age = 40
	cut.age = 69
	cut.weight = 141.58
	cut.height = 157.22

def test_case_6():
	cut = calorie_intake_calc(88.23,217.11,45,'F',0.41,'N')
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.weight = 88.69
	cut.weight = 158.58
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.gender = 'F'

def test_case_7():
	cut = calorie_intake_calc(68.07,217.07,68,'F',-0.5,'L')
	cut.amount_exercise = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_8():
	cut = calorie_intake_calc(46.64,184.79,60,'F',0.56,'L')
	cut.age = 82
	cut.height = 141.22
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.53
	cut.amount_exercise = 'E'

def test_case_9():
	cut = calorie_intake_calc(133.8,148.04,53,'M',-0.4,'N')
	cut.age = 44
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 187.6
	cut.gender = 'N'
	cut.bodyfat = -0.15
	cut.height = 155.64
	cut.weight = 145.21
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	cut.height = 202.25

