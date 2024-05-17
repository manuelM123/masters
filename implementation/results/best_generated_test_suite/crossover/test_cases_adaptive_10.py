from cut import *

def test_case_0():
	cut = calorie_intake_calc(141.67,153.28,42,'N',-0.1,'M')
	cut.bodyfat = 0.21
	cut.gender = 'M'
	cut.amount_exercise = 'V'
	cut.gender = 'N'
	cut.amount_exercise = 'N'
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_1():
	cut = calorie_intake_calc(43.62,212.87,36,'M',0.6,'M')
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = -0.46
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'L'

def test_case_2():
	cut = calorie_intake_calc(141.41,219.87,77,'N',0.75,'E')
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(78.49,187.82,66,'M',-0.07,'L')
	cut.amount_exercise = 'E'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'

def test_case_4():
	cut = calorie_intake_calc(189.18,136.57,43,'F',0.66,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 87.69
	cut.bodyfat = 0.18
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'F'
	cut.gender = 'N'
	cut.height = 159.84
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 87.87

def test_case_5():
	cut = calorie_intake_calc(140.32,201.15,85,'N',-0.16,'L')
	cut.amount_exercise = 'L'
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.bodyfat = 0.4
	cut.gender = 'F'
	cut.amount_exercise = 'E'

def test_case_6():
	cut = calorie_intake_calc(80.15,164.84,58,'M',0.03,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.3
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_determine_calorie_intake = cut.determine_calorie_intake()

def test_case_7():
	cut = calorie_intake_calc(72.52,166.49,28,'N',0.45,'N')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.amount_exercise = 'E'
	cut.age = 69
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.gender = 'M'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.age = 72

