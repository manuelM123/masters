from cut import *

def test_case_0():
	cut = calorie_intake_calc(198.44,199.44,28,'F',-0.28,'S')
	cut.age = 61
	cut.bodyfat = 0.39
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 210.96
	cut.gender = 'F'
	cut.bodyfat = -0.03

def test_case_1():
	cut = calorie_intake_calc(204.96,221.43,79,'N',-0.24,'E')

def test_case_2():
	cut = calorie_intake_calc(139.27,196.09,57,'M',-0.12,'E')
	cut.age = 84
	cut.bodyfat = 0.63
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'V'
	cut.height = 146.84
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

def test_case_3():
	cut = calorie_intake_calc(105.2,213.02,62,'N',-0.13,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 183.32

def test_case_4():
	cut = calorie_intake_calc(109.8,222.18,58,'N',0.34,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.1
	cut.age = 5
	cut.height = 158.72
	cut.height = 180.48
	cut.height = 170.23
	cut.gender = 'N'
	cut.height = 171.77
	cut.height = 221.99
	cut.bodyfat = 0.26

def test_case_5():
	cut = calorie_intake_calc(102.92,137.61,80,'F',0.22,'E')
	cut.amount_exercise = 'E'
	cut.weight = 76.65
	cut.height = 179.36

def test_case_6():
	cut = calorie_intake_calc(59.04,213.28,20,'F',0.7,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(210.29,216.55,79,'N',-0.09,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 36
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.age = 46

def test_case_8():
	cut = calorie_intake_calc(206.46,148.13,40,'F',0.02,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.45
	cut.gender = 'M'
	cut.gender = 'M'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 73.93
	cut.weight = 156.07

def test_case_9():
	cut = calorie_intake_calc(151.21,160.76,81,'F',-0.17,'M')
	cut.bodyfat = -0.22

def test_case_10():
	cut = calorie_intake_calc(140.4,164.03,53,'M',-0.42,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.23
	cut.gender = 'F'
	cut.height = 135.79
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'

