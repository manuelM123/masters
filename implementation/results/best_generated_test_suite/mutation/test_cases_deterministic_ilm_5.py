from cut import *

def test_case_0():
	cut = calorie_intake_calc(119.82,222.59,33,'N',0.04,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.71
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 158.73

def test_case_1():
	cut = calorie_intake_calc(159.42,223.16,11,'N',0.25,'M')
	cut.bodyfat = -0.13
	cut.height = 214.22
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.amount_exercise = 'L'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.age = 24
	cut.bodyfat = 0.09
	cut.weight = 75.48

def test_case_2():
	cut = calorie_intake_calc(209.05,182.78,45,'F',-0.13,'V')
	cut.bodyfat = -0.26
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.46
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_3():
	cut = calorie_intake_calc(178.9,213.74,15,'M',-0.4,'L')
	cut.weight = 178.11
	cut.weight = 120.32
	cut.height = 161.71
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 78
	cut.age = 55
	cut.bodyfat = 0.51
	cut.age = 19
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(208.04,175.03,38,'F',0.13,'S')
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(164.59,187.63,69,'F',-0.23,'N')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.13
	cut.amount_exercise = 'M'
	cut.bodyfat = -0.01

def test_case_6():
	cut = calorie_intake_calc(93.78,216.18,83,'N',-0.07,'V')
	cut.age = 22
	cut.weight = 92.45

def test_case_7():
	cut = calorie_intake_calc(141.89,209.45,24,'N',-0.07,'N')
	cut.bodyfat = -0.14
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 220.56
	cut.age = 36
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'S'

