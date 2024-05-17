from cut import *

def test_case_0():
	cut = calorie_intake_calc(63.38,220.35,19,'M',0.32,'S')
	cut.age = 25
	cut.bodyfat = -0.25
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.amount_exercise = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.53
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 162.99
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(209.19,167.15,13,'M',0.76,'L')
	cut.height = 156.76
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_2():
	cut = calorie_intake_calc(212.39,199.5,72,'M',-0.28,'S')
	cut.amount_exercise = 'M'

def test_case_3():
	cut = calorie_intake_calc(112.25,218.16,20,'N',0.03,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 221.86
	cut.amount_exercise = 'M'
	cut.height = 140.43
	cut.bodyfat = -0.47
	cut.weight = 162.42
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 164.4
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_4():
	cut = calorie_intake_calc(151.41,149.71,45,'M',0.01,'M')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = -0.22
	cut.age = 43
	cut.height = 201.7
	cut.age = 47
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'S'
	cut.age = 16
	cut.height = 139.45

