from cut import *

def test_case_0():
	cut = calorie_intake_calc(201.11,156.81,45,'F',-0.44,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.32
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'S'
	cut.amount_exercise = 'V'
	cut.amount_exercise = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'

def test_case_1():
	cut = calorie_intake_calc(129.39,200.26,44,'F',0.3,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 178.53
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 165.48
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_2():
	cut = calorie_intake_calc(167.13,188.43,53,'F',-0.24,'L')
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'M'
	result_tdee_calculation = cut.tdee_calculation()
	cut.age = 10
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'E'
	cut.weight = 39.3

def test_case_3():
	cut = calorie_intake_calc(157.95,205.75,19,'F',0.59,'M')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.gender = 'M'
	cut.bodyfat = 0.76
	cut.weight = 86.55
	cut.age = 20
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.02

def test_case_4():
	cut = calorie_intake_calc(76.92,217.31,79,'F',-0.31,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 224.47
	cut.height = 151.27
	cut.weight = 202.18

def test_case_5():
	cut = calorie_intake_calc(85.52,189.83,31,'F',-0.21,'N')
	cut.amount_exercise = 'N'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(187.56,162.48,17,'F',-0.3,'S')
	cut.age = 7
	cut.bodyfat = 0.08
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'N'
	cut.bodyfat = -0.12
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.44

