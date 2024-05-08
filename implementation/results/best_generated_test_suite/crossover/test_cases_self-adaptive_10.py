from cut import *

def test_case_0():
	cut = calorie_intake_calc(214.94,171.57,68,'N',0.2,'L')
	cut.bodyfat = -0.2
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.4
	cut.amount_exercise = 'M'
	cut.amount_exercise = 'E'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 156.55
	cut.bodyfat = 0.08
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_1():
	cut = calorie_intake_calc(51.37,165.16,66,'F',0.59,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 140.34
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 143.69
	cut.bodyfat = -0.19
	cut.weight = 121.32
	cut.age = 81

def test_case_2():
	cut = calorie_intake_calc(78.22,189.03,73,'M',-0.28,'S')

def test_case_3():
	cut = calorie_intake_calc(54.17,148.21,25,'M',0.48,'E')
	cut.age = 12
	cut.weight = 111.93
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.36
	cut.amount_exercise = 'M'

def test_case_4():
	cut = calorie_intake_calc(96.63,185.74,33,'F',0.5,'S')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'F'
	cut.gender = 'N'
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 160.69
	cut.gender = 'N'
	cut.height = 175.37
	cut.weight = 162.31
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(196.09,135.2,70,'F',0.16,'M')
	cut.weight = 60.11
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.age = 59
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

def test_case_6():
	cut = calorie_intake_calc(74.64,164.54,15,'F',-0.18,'S')
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'
	cut.gender = 'F'
	cut.bodyfat = -0.01
	cut.amount_exercise = 'N'
	cut.height = 159.26
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_7():
	cut = calorie_intake_calc(204.76,216.27,40,'M',-0.34,'E')
	cut.amount_exercise = 'M'
	cut.weight = 155.42
	cut.bodyfat = 0.5
	cut.bodyfat = -0.26
	cut.age = 48
	cut.gender = 'F'
	cut.height = 187.12
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.gender = 'M'

def test_case_8():
	cut = calorie_intake_calc(124.14,193.25,60,'M',-0.27,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 31
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()

