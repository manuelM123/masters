from cut import *

def test_case_0():
	cut = calorie_intake_calc(162.94,188.11,29,'F',0.29,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.gender = 'N'
	cut.bodyfat = -0.32

def test_case_1():
	cut = calorie_intake_calc(201.88,145.38,56,'M',-0.44,'E')
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 191.86
	cut.bodyfat = 0.73
	cut.weight = 139.76

def test_case_2():
	cut = calorie_intake_calc(83.7,185.5,49,'F',0.57,'E')
	cut.amount_exercise = 'S'
	cut.weight = 137.6

def test_case_3():
	cut = calorie_intake_calc(102.02,170.9,85,'N',-0.11,'M')

def test_case_4():
	cut = calorie_intake_calc(156.53,145.01,48,'F',0.68,'M')
	cut.amount_exercise = 'V'
	cut.gender = 'F'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_5():
	cut = calorie_intake_calc(62.6,176.29,75,'F',-0.02,'M')
	result_tdee_calculation = cut.tdee_calculation()
	cut.amount_exercise = 'L'
	result_tdee_calculation = cut.tdee_calculation()

def test_case_6():
	cut = calorie_intake_calc(207.25,174.21,46,'N',-0.21,'M')
	cut.amount_exercise = 'S'
	cut.weight = 162.47
	result_tdee_calculation = cut.tdee_calculation()
	cut.weight = 84.44

