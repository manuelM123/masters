from cut import *

def test_case_0():
	cut = calorie_intake_calc(68.64,213.73,75,'N',0.21,'E')
	cut.weight = 159.43
	result_tdee_calculation = cut.tdee_calculation()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.13
	result_tdee_calculation = cut.tdee_calculation()
	cut.height = 191.55

def test_case_1():
	cut = calorie_intake_calc(171.1,156.7,24,'M',0.25,'E')
	cut.bodyfat = 0.22
	cut.weight = 108.62

def test_case_2():
	cut = calorie_intake_calc(70.57,201.03,56,'F',0.14,'L')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_tdee_calculation = cut.tdee_calculation()
	cut.bodyfat = 0.21
	result_determine_calorie_intake = cut.determine_calorie_intake()
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.height = 197.15
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()

def test_case_3():
	cut = calorie_intake_calc(96.6,159.65,79,'M',0.02,'E')
	result_mifflin_stjeor_equation = cut.mifflin_stjeor_equation()
	cut.weight = 131.62
	cut.bodyfat = 0.09
	result_determine_calorie_intake = cut.determine_calorie_intake()
	cut.amount_exercise = 'V'
	result_tdee_calculation = cut.tdee_calculation()
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.gender = 'N'

def test_case_4():
	cut = calorie_intake_calc(85.34,170.75,67,'N',0.12,'M')
	cut.gender = 'F'
	cut.height = 186.26
	cut.bodyfat = 0.06
	cut.weight = 146.01
	cut.amount_exercise = 'N'
	result_katch_mcardle_equation = cut.katch_mcardle_equation()
	cut.weight = 146.99

