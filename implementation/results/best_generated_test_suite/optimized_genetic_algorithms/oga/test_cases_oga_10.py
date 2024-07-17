from cut import *

def test_case_0():
	cut = calorie_intake_calc(165.4,166.44,8,'F',0.68,'V')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.height = 141.5

def test_case_1():
	cut = calorie_intake_calc(105.01,141.85,34,'M',-0.42,'E')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'N'

def test_case_2():
	cut = calorie_intake_calc(150.38,148.33,33,'N',-0.21,'S')
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = -0.36

def test_case_3():
	cut = calorie_intake_calc(157.45,139.45,13,'F',0.42,'V')
	cut.gender = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.height = 196.52
	cut.height = 145.78

def test_case_4():
	cut = calorie_intake_calc(177.46,202.81,25,'N',0.79,'S')
	cut.weight = 196.13
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.bodyfat = 0.01

def test_case_5():
	cut = calorie_intake_calc(131.04,159.62,44,'F',-0.37,'S')
	cut.height = 167.62
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 144.66

